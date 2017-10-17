#SBaaS
from .stage03_quantification_tfba_io import stage03_quantification_tfba_io
from .stage03_quantification_measuredData_query import stage03_quantification_measuredData_query
from .stage03_quantification_dG_f_query import stage03_quantification_dG_f_query
from .stage03_quantification_dG_r_query import stage03_quantification_dG_r_query
from .stage03_quantification_otherData_query import stage03_quantification_otherData_query
from .stage03_quantification_simulation_query import stage03_quantification_simulation_query
from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
# Dependencies from thermodynamics
from thermodynamics.thermodynamics_dG_f_data import thermodynamics_dG_f_data
from thermodynamics.thermodynamics_dG_r_data import thermodynamics_dG_r_data
from thermodynamics.thermodynamics_metabolomicsData import thermodynamics_metabolomicsData
from thermodynamics.thermodynamics_otherData import thermodynamics_otherData
from thermodynamics.thermodynamics_simulatedData import thermodynamics_simulatedData
from thermodynamics.thermodynamics_tfba import thermodynamics_tfba
# Dependencies from resources
from sampling.sampling import cobra_sampling
from sampling.sampling_statistics import cobra_sampling,cobra_sampling_n
from cobra.manipulation.modify import convert_to_irreversible

class stage03_quantification_tfba_execute(stage03_quantification_tfba_io,
                                          stage03_quantification_measuredData_query,
                                          stage03_quantification_dG_f_query,
                                          stage03_quantification_dG_r_query,
                                          stage03_quantification_otherData_query,
                                          stage03_quantification_simulation_query):
    def execute_thermodynamicSampling(self,simulation_id_I,models_I,
                    data_dir_I,rxn_ids_I=[],
                    inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                    inconsistent_tcc_I=[],
                    measured_concentration_coverage_criteria_I=0.5,
                    measured_dG_f_coverage_criteria_I=0.99,
                    solver_I='glpk'):
        '''execute a thermodynamic analysis using the thermodynamic
        module for cobrapy

        Input:
           inconsistent_dG_f_I = dG_f measured values to be substituted for estimated values
           inconsistent_concentrations_I = concentration measured values to be substituted for estimated values
           inconsistent_tcc_I = reactions considered feasible to be changed to infeasible so that dG0_r constraints do not break the model
           measured_concentration_coverage_criteria_I = float, minimum concentration coverage to consider for feasibility
           measured_dG_f_coveragea_criteria_I = float, minimum dG_f coverage to consider for feasibility
           data_dir_I = directory of sampled points
           solver_I = string, solver name
        '''
        modelsCOBRA = models_COBRA_dependencies();
        print('execute_thermodynamicSampling...')
        # get simulation information
        simulation_info_all = [];
        simulation_info_all = self.get_rows_simulationIDAndSimulationType_dataStage03QuantificationSimulation(simulation_id_I,'sampling')
        if not simulation_info_all:
            print('simulation not found!')
            return;
        simulation_info = simulation_info_all[0]; # unique constraint guarantees only 1 row will be returned
        # get simulation parameters
        simulation_parameters_all = [];
        simulation_parameters_all = self.get_rows_simulationID_dataStage03QuantificationSimulationParameters(simulation_id_I);
        if not simulation_parameters_all:
            print('simulation not found!')
            return;
        simulation_parameters = simulation_parameters_all[0]; # unique constraint guarantees only 1 row will be returned
        # get the cobra model
        cobra_model = models_I[simulation_info['model_id']];
        # copy the model
        cobra_model_copy = cobra_model.copy();
        # get rxn_ids
        if rxn_ids_I:
            rxn_ids = rxn_ids_I;
        else:
            rxn_ids = [];
            rxn_ids = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['sample_name_abbreviation']);
        for rxn in rxn_ids:
            # constrain the model
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).lower_bound = rxn['flux_lb'];
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).upper_bound = rxn['flux_ub'];
        # make the model irreversible
        convert_to_irreversible(cobra_model_copy);
        # get otherData
        pH,temperature,ionic_strength = {},{},{}
        pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load pH, ionic_strength, and temperature parameters
        other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
        other_data.check_data();
        # get dG_f data:
        dG_f = {};
        dG_f = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        dG_f_data = thermodynamics_dG_f_data(dG_f_I=dG_f);
        dG_f_data.format_dG_f();
        dG_f_data.generate_estimated_dG_f(cobra_model)
        dG_f_data.check_data(); 
        # remove an inconsistent dGf values
        if inconsistent_dG_f_I: dG_f_data.remove_measured_dG_f(inconsistent_dG_f_I)
        # query metabolomicsData
        concentrations = [];
        concentrations = self.get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load metabolomicsData
        metabolomics_data = thermodynamics_metabolomicsData(measured_concentrations_I=concentrations);
        metabolomics_data.generate_estimated_metabolomics_data(cobra_model);
        # remove an inconsistent concentration values
        if inconsistent_concentrations_I: metabolomics_data.remove_measured_concentrations(inconsistent_concentrations_I);
        # get dG0r, dGr, and tcc data
        dG0_r = {};
        dG0_r = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'])
        measured_concentration_coverage,measured_dG_f_coverage,feasible = {},{},{};
        measured_concentration_coverage,measured_dG_f_coverage,feasible = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'],0,0)
        tcc = thermodynamics_dG_r_data(dG0_r_I = dG0_r,
                 dG_r_coverage_I = measured_dG_f_coverage,
                 metabolomics_coverage_I = measured_concentration_coverage,
                 thermodynamic_consistency_check_I = feasible);
        if inconsistent_tcc_I: tcc.change_feasibleReactions(inconsistent_tcc_I);
        # apply tfba constraints
        tfba = thermodynamics_tfba()
        tfba._add_conc_ln_constraints_transport(cobra_model_copy, metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations,
                                             tcc.dG0_r, other_data.pH,other_data.temperature,tcc.metabolomics_coverage,
                                             tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
                                             measured_concentration_coverage_criteria_I, measured_dG_f_coverage_criteria_I,
                                             use_measured_concentrations=True,use_measured_dG0_r=True);
        # Test model
        if modelsCOBRA.test_model(cobra_model_I=cobra_model_copy):
            sampling = cobra_sampling(data_dir_I = data_dir_I);
            if simulation_parameters['sampler_id']=='gpSampler':
                filename_model = simulation_id_I + '.mat';
                filename_script = simulation_id_I + '.m';
                filename_points = simulation_id_I + '_points' + '.mat';
                sampling.export_sampling_matlab(cobra_model=cobra_model_copy,filename_model=filename_model,filename_script=filename_script,filename_points=filename_points,\
                    solver_id_I = simulation_parameters['solver_id'],\
                    n_points_I = simulation_parameters['n_points'],\
                    n_steps_I = simulation_parameters['n_steps'],\
                    max_time_I = simulation_parameters['max_time']);
            elif simulation_parameters['sampler_id']=='optGpSampler':
                return;
            else:
                print('sampler_id not recognized');
        else:
            print('no solution found!');  

    def check_thermodynamicConstraints(self,simulation_id_I,models_I,rxn_ids_I=[],
                    inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                    measured_concentration_coverage_criteria_I=0.5,
                    measured_dG_f_coverage_criteria_I=0.99,
                    n_checks_I = 5,
                    diagnose_solver_I='glpk',diagnose_threshold_I=0.98,diagnose_break_I=0.1):
        
        print('check_thermodynamicConstraints...')
        # get simulation information
        simulation_info_all = [];
        simulation_info_all = self.get_rows_simulationID_dataStage03QuantificationSimulation(simulation_id_I);
        if not simulation_info_all:
            print('simulation not found!')
            return;
        simulation_info = simulation_info_all[0]; # unique constraint guarantees only 1 row will be returned
        # get simulation parameters
        simulation_parameters_all = [];
        simulation_parameters_all = self.get_rows_simulationID_dataStage03QuantificationSimulationParameters(simulation_id_I);
        if not simulation_parameters_all:
            print('simulation not found!')
            return;
        simulation_parameters = simulation_parameters_all[0]; # unique constraint guarantees only 1 row will be returned
        # get the cobra model
        cobra_model = models_I[simulation_info['model_id']];
        # copy the model
        cobra_model_copy = cobra_model.copy();
        # get rxn_ids
        if rxn_ids_I:
            rxn_ids = rxn_ids_I;
        else:
            rxn_ids = [];
            rxn_ids = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['sample_name_abbreviation']);
        for rxn in rxn_ids:
            # constrain the model
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).lower_bound = rxn['flux_lb'];
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).upper_bound = rxn['flux_ub'];
        # make the model irreversible
        convert_to_irreversible(cobra_model_copy);
        # get otherData
        pH,temperature,ionic_strength = {},{},{}
        pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load pH, ionic_strength, and temperature parameters
        other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
        other_data.check_data();
        # get dG_f data:
        dG_f = {};
        dG_f = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        dG_f_data = thermodynamics_dG_f_data(dG_f_I=dG_f);
        dG_f_data.format_dG_f();
        dG_f_data.generate_estimated_dG_f(cobra_model)
        dG_f_data.check_data(); 
        # remove an inconsistent dGf values
        if inconsistent_dG_f_I: dG_f_data.remove_measured_dG_f(inconsistent_dG_f_I)
        # query metabolomicsData
        concentrations = [];
        concentrations = self.get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load metabolomicsData
        metabolomics_data = thermodynamics_metabolomicsData(measured_concentrations_I=concentrations);
        metabolomics_data.generate_estimated_metabolomics_data(cobra_model);
        # remove an inconsistent concentration values
        if inconsistent_concentrations_I: metabolomics_data.remove_measured_concentrations(inconsistent_concentrations_I);
        # get dG0r, dGr, and tcc data
        dG0_r = {};
        dG0_r = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'])
        measured_concentration_coverage,measured_dG_f_coverage,feasible = {},{},{};
        measured_concentration_coverage,measured_dG_f_coverage,feasible = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'],0,0)
        tcc = thermodynamics_dG_r_data(dG0_r_I = dG0_r,
                 dG_r_coverage_I = measured_dG_f_coverage,
                 metabolomics_coverage_I = measured_concentration_coverage,
                 thermodynamic_consistency_check_I = feasible);
        # apply tfba constraints
        tfba = thermodynamics_tfba()
        thermodynamic_constraints_check,diagnose_variables_1,diagnose_variables_2,diagnose_variables_3 = tfba.check_conc_ln_constraints_transport(cobra_model_copy,
                                             metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations,
                                             tcc.dG0_r, other_data.pH,other_data.temperature,tcc.metabolomics_coverage,
                                             tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
                                             measured_concentration_coverage_criteria_I, measured_dG_f_coverage_criteria_I,
                                             n_checks_I = 5,
                                             diagnose_solver_I=None,diagnose_threshold_I=0.98,diagnose_break_I=0.1);

        return thermodynamic_constraints_check,diagnose_variables_1,diagnose_variables_2,diagnose_variables_3;
    def execute_analyzeThermodynamicSamplingPoints(self,simulation_id_I,models_I,
                    data_dir_I,data_dir_O,rxn_ids_I=[],
                    inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                    inconsistent_tcc_I=[],
                    measured_concentration_coverage_criteria_I=0.5,
                    measured_dG_f_coverage_criteria_I=0.99,
                    remove_pointsNotInSolutionSpace_I=True,
                    min_pointsInSolutionSpace_I=1000):
        '''Load and analyze sampling points

        Input:
           inconsistent_dG_f_I = dG_f measured values to be substituted for estimated values
           inconsistent_concentrations_I = concentration measured values to be substituted for estimated values
           inconsistent_tcc_I = reactions considered feasible to be changed to infeasible so that dG0_r constraints do not break the model
           measured_concentration_coverage_criteria_I = float, minimum concentration coverage to consider for feasibility
           measured_dG_f_coveragea_criteria_I = float, minimum dG_f coverage to consider for feasibility
           remove_pointsNotInSolutionSpace_I = boolean, remove points not in the solution space (i.e., within the lower/upper bounds)
           min_pointsInSolutionSpace_I = int, minimum number of points in the solution space.
                                        if the number of points is less that the minimum, the solution space will be increased by
                                        (upper_bounds-lower_bounds)/4 until the minimum number of points is met
           data_dir_I = directory of sampled points
           data_dir_O = director to write QC'd sampled points
           solver_I = string, solver name
           
           '''

        print('analyzing sampling points');
        
        modelsCOBRA = models_COBRA_dependencies();
        # get simulation information
        simulation_info_all = [];
        simulation_info_all = self.get_rows_simulationIDAndSimulationType_dataStage03QuantificationSimulation(simulation_id_I,'sampling')
        if not simulation_info_all:
            print('simulation not found!')
            return;
        simulation_info = simulation_info_all[0]; # unique constraint guarantees only 1 row will be returned
        # get simulation parameters
        simulation_parameters_all = [];
        simulation_parameters_all = self.get_rows_simulationID_dataStage03QuantificationSimulationParameters(simulation_id_I);
        if not simulation_parameters_all:
            print('simulation not found!')
            return;
        simulation_parameters = simulation_parameters_all[0]; # unique constraint guarantees only 1 row will be returned
        # get the cobra model
        cobra_model = models_I[simulation_info['model_id']];
        # copy the model
        cobra_model_copy = cobra_model.copy();
        # get rxn_ids
        if rxn_ids_I:
            rxn_ids = rxn_ids_I;
        else:
            rxn_ids = [];
            rxn_ids = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['sample_name_abbreviation']);
        for rxn in rxn_ids:
            # constrain the model
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).lower_bound = rxn['flux_lb'];
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).upper_bound = rxn['flux_ub'];
        # make the model irreversible
        convert_to_irreversible(cobra_model_copy);
        # get otherData
        pH,temperature,ionic_strength = {},{},{}
        pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load pH, ionic_strength, and temperature parameters
        other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
        other_data.check_data();
        # get dG_f data:
        dG_f = {};
        dG_f = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        dG_f_data = thermodynamics_dG_f_data(dG_f_I=dG_f);
        dG_f_data.format_dG_f();
        dG_f_data.generate_estimated_dG_f(cobra_model)
        dG_f_data.check_data(); 
        # remove an inconsistent dGf values
        if inconsistent_dG_f_I: dG_f_data.remove_measured_dG_f(inconsistent_dG_f_I)
        # query metabolomicsData
        concentrations = [];
        concentrations = self.get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load metabolomicsData
        metabolomics_data = thermodynamics_metabolomicsData(measured_concentrations_I=concentrations);
        metabolomics_data.generate_estimated_metabolomics_data(cobra_model);
        # remove an inconsistent concentration values
        if inconsistent_concentrations_I: metabolomics_data.remove_measured_concentrations(inconsistent_concentrations_I);
        # get dG0r, dGr, and tcc data
        dG0_r = {};
        dG0_r = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'])
        measured_concentration_coverage,measured_dG_f_coverage,feasible = {},{},{};
        measured_concentration_coverage,measured_dG_f_coverage,feasible = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'],0,0)
        tcc = thermodynamics_dG_r_data(dG0_r_I = dG0_r,
                 dG_r_coverage_I = measured_dG_f_coverage,
                 metabolomics_coverage_I = measured_concentration_coverage,
                 thermodynamic_consistency_check_I = feasible);
        if inconsistent_tcc_I: tcc.change_feasibleReactions(inconsistent_tcc_I);
        # apply tfba constraints
        tfba = thermodynamics_tfba()
        tfba._add_conc_ln_constraints_transport(cobra_model_copy, metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations,
                                             tcc.dG0_r, other_data.pH,other_data.temperature,tcc.metabolomics_coverage,
                                             tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
                                             measured_concentration_coverage_criteria_I, measured_dG_f_coverage_criteria_I,
                                             use_measured_concentrations=True,use_measured_dG0_r=True);
        # Test each model
        if modelsCOBRA.test_model(cobra_model_I=cobra_model_copy):
            sampling = cobra_sampling(data_dir_I = data_dir_I,model_I = cobra_model_copy);
            if simulation_parameters['sampler_id']=='gpSampler':
                # load the results of sampling
                filename_points = simulation_id_I + '_points' + '.mat';
                sampling.get_points_matlab(filename_points,'sampler_out');
                # check if points were sampled outside the solution space
                if remove_pointsNotInSolutionSpace_I:
                    pruned_reactions = sampling.remove_points_notInSolutionSpace(min_points_I=min_pointsInSolutionSpace_I);
                ## check if the model contains loops
                #sampling.simulate_loops(data_fva=settings.workspace_data + '/loops_fva_tmp.json');
                #sampling.find_loops(data_fva=settings.workspace_data + '/loops_fva_tmp.json');
                #sampling.remove_loopsFromPoints();
                sampling.descriptive_statistics();
            elif simulation_parameters['sampler_id']=='optGpSampler':
                return;
            else:
                print('sampler_id not recognized');
            # add data to the database
            row = {'simulation_id':simulation_id_I,
                'simulation_dateAndTime':sampling.simulation_dateAndTime,
                'mixed_fraction':sampling.mixed_fraction,
                'data_dir':data_dir_I+'/'+filename_points,
                'infeasible_loops':sampling.loops,
                'used_':True,
                'comment_':None
                };
            self.add_dataStage03QuantificationSampledPoints([row])
            #row = None;
            #row = data_stage03_quantification_sampledPoints(
            #    simulation_id_I,
            #    sampling.simulation_dateAndTime,
            #    sampling.mixed_fraction,
            #    data_dir_I+'/'+filename_points,
            #    sampling.loops,
            #    True,
            #    None);
            #self.session.add(row);
            # write points to json file

            # add data to the database
            sampledData_O = [];
            for k,v in sampling.points_statistics.items():
                type,units = tfba.get_variableTypeAndUnits(k);
                row = {'simulation_id':simulation_id_I,
                    'simulation_dateAndTime':sampling.simulation_dateAndTime,
                    'variable_id':k,
                    'variable_type':type,
                    'variable_units':units,
                    'sampling_points':None, #v['points'],
                    'sampling_ave':v['ave'],
                    'sampling_var':v['var'],
                    'sampling_lb':v['lb'],
                    'sampling_ub':v['ub'],
                    'sampling_ci':0.95,
                    'sampling_min':v['min'],
                    'sampling_max':v['max'],
                    'sampling_median':v['median'],
                    'sampling_iq_1':v['iq_1'],
                    'sampling_iq_3':v['iq_3'],
                    'used_':True,
                    'comment_':None};
                sampledData_O.append(row);
                #row = None;
                #row = data_stage03_quantification_sampledData(
                #    simulation_id_I,
                #    sampling.simulation_dateAndTime,
                #    k,
                #    type,
                #    units,
                #    None, #v['points'],
                #    v['ave'],
                #    v['var'],
                #    v['lb'],
                #    v['ub'],
                #    v['min'],
                #    0.95,
                #    v['max'],
                #    v['median'],
                #    v['iq_1'],
                #    v['iq_3'],
                #    True,
                #    None);
                #self.session.add(row);
            self.add_dataStage03QuantificationSampledData(sampledData_O);
        else:
            print('no solution found!'); 
    def execute_tfba(self,simulation_id_I,models_I,
                    data_dir_I,rxn_ids_I=[],
                    inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                    inconsistent_tcc_I=[],
                    measured_concentration_coverage_criteria_I=0.5,
                    measured_dG_f_coverage_criteria_I=0.99,
                    solver_I='glpk'):
        '''execute a thermodynamic flux balance analysis using the thermodynamic
        module for cobrapy

        Input:
           inconsistent_dG_f_I = dG_f measured values to be substituted for estimated values
           inconsistent_concentrations_I = concentration measured values to be substituted for estimated values
           inconsistent_tcc_I = reactions considered feasible to be changed to infeasible so that dG0_r constraints do not break the model
           measured_concentration_coverage_criteria_I = float, minimum concentration coverage to consider for feasibility
           measured_dG_f_coveragea_criteria_I = float, minimum dG_f coverage to consider for feasibility
           solver_I = string, solver name
        '''
        
    def execute_tfva(self,simulation_id_I,models_I,
                    data_dir_I,rxn_ids_I=[],
                    inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                    inconsistent_tcc_I=[],
                    measured_concentration_coverage_criteria_I=0.5,
                    measured_dG_f_coverage_criteria_I=0.99,
                    solver_I='glpk'):
        '''execute a thermodynamic flux variability analysis on the reaction variables
        using the thermodynamic module for cobrapy

        Input:
           inconsistent_dG_f_I = dG_f measured values to be substituted for estimated values
           inconsistent_concentrations_I = concentration measured values to be substituted for estimated values
           inconsistent_tcc_I = reactions considered feasible to be changed to infeasible so that dG0_r constraints do not break the model
           measured_concentration_coverage_criteria_I = float, minimum concentration coverage to consider for feasibility
           measured_dG_f_coveragea_criteria_I = float, minimum dG_f coverage to consider for feasibility
           solver_I = string, solver name
        '''
        
        data_O = []
        modelsCOBRA = models_COBRA_dependencies();
        # get simulation information
        simulation_info_all = [];
        simulation_info_all = self.get_rows_simulationIDAndSimulationType_dataStage03QuantificationSimulation(simulation_id_I,'sampling')
        if not simulation_info_all:
            print('simulation not found!')
            return;
        simulation_info = simulation_info_all[0]; # unique constraint guarantees only 1 row will be returned
        # get simulation parameters
        simulation_parameters_all = [];
        simulation_parameters_all = self.get_rows_simulationID_dataStage03QuantificationSimulationParameters(simulation_id_I);
        if not simulation_parameters_all:
            print('simulation not found!')
            return;
        simulation_parameters = simulation_parameters_all[0]; # unique constraint guarantees only 1 row will be returned
        # get the cobra model
        cobra_model = models_I[simulation_info['model_id']];
        # copy the model
        cobra_model_copy = cobra_model.copy();
        # get rxn_ids
        if rxn_ids_I:
            rxn_ids = rxn_ids_I;
        else:
            rxn_ids = [];
            rxn_ids = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['sample_name_abbreviation']);
        for rxn in rxn_ids:
            # constrain the model
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).lower_bound = rxn['flux_lb'];
            cobra_model_copy.reactions.get_by_id(rxn['rxn_id']).upper_bound = rxn['flux_ub'];
        # make the model irreversible
        convert_to_irreversible(cobra_model_copy); #TODO ensure that the model is irreversible before!
        # get otherData
        pH,temperature,ionic_strength = {},{},{}
        pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load pH, ionic_strength, and temperature parameters
        other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
        other_data.check_data();
        # get dG_f data:
        dG_f = {};
        dG_f = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        dG_f_data = thermodynamics_dG_f_data(dG_f_I=dG_f);
        dG_f_data.format_dG_f();
        dG_f_data.generate_estimated_dG_f(cobra_model)
        dG_f_data.check_data(); 
        # remove an inconsistent dGf values
        if inconsistent_dG_f_I: dG_f_data.remove_measured_dG_f(inconsistent_dG_f_I)
        # query metabolomicsData
        concentrations = [];
        concentrations = self.get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(simulation_info['experiment_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation']);
        # load metabolomicsData
        metabolomics_data = thermodynamics_metabolomicsData(measured_concentrations_I=concentrations);
        metabolomics_data.generate_estimated_metabolomics_data(cobra_model);
        # remove an inconsistent concentration values
        if inconsistent_concentrations_I: metabolomics_data.remove_measured_concentrations(inconsistent_concentrations_I);
        # get dG0r, dGr, and tcc data
        dG0_r = {};
        dG0_r = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'])
        dG_r = {};
        dG_r = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'])
        measured_concentration_coverage,measured_dG_f_coverage,feasible = {},{},{};
        measured_concentration_coverage,measured_dG_f_coverage,feasible = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'],0,0)
        tcc = thermodynamics_dG_r_data(dG0_r_I = dG0_r,
                    dG_r_I = dG_r,
                 dG_r_coverage_I = measured_dG_f_coverage,
                 metabolomics_coverage_I = measured_concentration_coverage,
                 thermodynamic_consistency_check_I = feasible);
        if inconsistent_tcc_I: tcc.change_feasibleReactions(inconsistent_tcc_I);
        
        tfba = thermodynamics_tfba()
        cobra_model_copy1 = cobra_model_copy.copy()
        tfba.tfva(cobra_model_copy1, 
            tcc.dG_r,#tcc.dG0_r,
            tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
            use_measured_dG0_r=True, reaction_list=None,fraction_of_optimum=1.0, solver=solver_I,
            objective_sense="maximize")

        tfba.analyze_tfva_results(threshold=1e-6)
        for k,v in tfba.tfva_data.items():
            analysis_list = []
            for k1,v1 in tfba.tfva_analysis[k].items():
                if v1:
                    analysis_list.append(k1)
            analysis_str = ';'.join(analysis_list)
            row = {'simulation_id':simulation_id_I,
            'simulation_dateAndTime':None,
            'variable_id':k,
            'variable_type':'flux',
            'variable_units':v['flux_units'],
            'fva_minimum':v['flux_lb'],
            'fva_maximum':v['flux_ub'],
            'fva_method':'tfva',
            'allow_loops':True,
            'fva_options':None,
            'solver_id':solver_I,
            'used_':True,
            'comment_':analysis_str}
            data_O.append(row)
            
        cobra_model_copy1 = cobra_model_copy.copy()
        tfba.tfva_dG_r(cobra_model_copy1,  
            tcc.dG_r,#tcc.dG0_r,
            tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
            use_measured_dG0_r=True, fraction_of_optimum=1.0, solver=solver_I,
            objective_sense="maximize")
        for k,v in tfba.tfva_dG_r_data.items():
            row = {'simulation_id':simulation_id_I,
            'simulation_dateAndTime':None,
            'variable_id':k,
            'variable_type':'dG_r',
            'variable_units':v['flux_units'],
            'fva_minimum':v['flux_lb'],
            'fva_maximum':v['flux_ub'],
            'fva_method':'tfva',
            'allow_loops':True,
            'fva_options':None,
            'solver_id':solver_I,
            'used_':True,
            'comment_':None}
            data_O.append(row)
            
        cobra_model_copy1 = cobra_model_copy.copy()
        tfba.tfva_concentrations(cobra_model_copy1, 
            metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations,
            tcc.dG0_r,other_data.temperature,tcc.metabolomics_coverage,
            tcc.dG_r_coverage, tcc.thermodynamic_consistency_check,
            measured_concentration_coverage_criteria = 0.5, measured_dG_f_coverage_criteria = 0.99,
            use_measured_concentrations=True,use_measured_dG0_r=True,fraction_of_optimum=1.0, solver=solver_I,
            objective_sense="maximize")
        for k,v in tfba.tfva_concentrations_data.items():
            row = {'simulation_id':simulation_id_I,
            'simulation_dateAndTime':None,
            'variable_id':k,
            'variable_type':'conc_ln',
            'variable_units':v['flux_units'],
            'fva_minimum':v['flux_lb'],
            'fva_maximum':v['flux_ub'],
            'fva_method':'tfva',
            'allow_loops':True,
            'fva_options':None,
            'solver_id':solver_I,
            'used_':True,
            'comment_':None}
            data_O.append(row)
        if data_O:
            self.add_rows_table('data_stage03_quantification_simulatedData_tfva',data_O);
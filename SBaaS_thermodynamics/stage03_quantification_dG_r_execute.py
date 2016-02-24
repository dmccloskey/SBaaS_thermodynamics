#SBaaS
from .stage03_quantification_dG_r_io import stage03_quantification_dG_r_io
from .stage03_quantification_measuredData_query import stage03_quantification_measuredData_query
from .stage03_quantification_dG_f_query import stage03_quantification_dG_f_query
from .stage03_quantification_simulatedData_query import stage03_quantification_simulatedData_query
from .stage03_quantification_otherData_query import stage03_quantification_otherData_query
from .stage03_quantification_simulation_query import stage03_quantification_simulation_query
# Dependencies from thermodynamics
from thermodynamics.thermodynamics_dG_f_data import thermodynamics_dG_f_data
from thermodynamics.thermodynamics_dG_r_data import thermodynamics_dG_r_data
from thermodynamics.thermodynamics_metabolomicsData import thermodynamics_metabolomicsData
from thermodynamics.thermodynamics_otherData import thermodynamics_otherData
from thermodynamics.thermodynamics_simulatedData import thermodynamics_simulatedData

class stage03_quantification_dG_r_execute(stage03_quantification_dG_r_io,
                                          stage03_quantification_measuredData_query,
                                          stage03_quantification_dG_f_query,
                                          stage03_quantification_simulatedData_query,
                                          stage03_quantification_otherData_query,
                                          stage03_quantification_simulation_query):
    def execute_calculate_dG_r(self,experiment_id_I,models_I,model_ids_I = [],
                            time_points_I=[],sample_name_abbreviations_I=[],
                            inconsistent_dG_f_I=[],inconsistent_concentrations_I=[],
                            measured_concentration_coverage_criteria_I=0.5,
                            measured_dG_f_coverage_criteria_I=0.99):

        '''calculate dG0_r, dG_r, displacements, and perform a thermodynamic consistency check'''
        dG0_r_O = [];
        dG_r_O = [];
        tcc_O = [];
        # get the model ids:
        if model_ids_I:
            model_ids = model_ids_I;
        else:
            model_ids = [];
            model_ids = self.get_modelID_experimentID_dataStage03QuantificationSimulation(experiment_id_I);
        for model_id in model_ids:
            # get the cobra model
            cobra_model = models_I[model_id];
            # get simulated data
            fva_data,sra_data = {},{};
            fva_data,sra_data = self.get_rowsDict_experimentIDAndModelID_dataStage03QuantificationSimulatedData(experiment_id_I,model_id);
            # load simulated data
            simulated_data = thermodynamics_simulatedData(fva_data_I=fva_data,sra_data_I=sra_data);
            simulated_data.check_data();
            # get the time-points
            if time_points_I:
                time_points = time_points_I;
            else:
                time_points = [];
                time_points = self.get_timePoints_experimentIDAndModelID_dataStage03QuantificationSimulation(experiment_id_I,model_id);
            for tp in time_points:
                # get sample_name_abbreviations
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndModelIDAndTimePoint_dataStage03QuantificationSimulation(experiment_id_I,model_id,tp);
                for sna in sample_name_abbreviations:
                    # get otherData
                    pH,temperature,ionic_strength = {},{},{}
                    pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(experiment_id_I,tp,sna);
                    # load pH, ionic_strength, and temperature parameters
                    other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
                    other_data.check_data();
                    # get dG_f data:
                    dG_f = {};
                    dG_f = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(experiment_id_I,model_id,tp,sna);
                    dG_f_data = thermodynamics_dG_f_data(dG_f_I=dG_f);
                    dG_f_data.format_dG_f();
                    dG_f_data.generate_estimated_dG_f(cobra_model)
                    dG_f_data.check_data(); 
                    # remove an inconsistent dGf values
                    if inconsistent_dG_f_I: dG_f_data.remove_measured_dG_f(inconsistent_dG_f_I)
                    # query metabolomicsData
                    concentrations = [];
                    concentrations = self.get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(experiment_id_I,tp,sna);
                    # load metabolomicsData
                    metabolomics_data = thermodynamics_metabolomicsData(measured_concentrations_I=concentrations);
                    metabolomics_data.generate_estimated_metabolomics_data(cobra_model);
                    # remove an inconsistent concentration values
                    if inconsistent_concentrations_I: metabolomics_data.remove_measured_concentrations(inconsistent_concentrations_I);
                    # calculate dG0r, dGr, displacements, and perform a thermodynamic consistency check based on model simulations
                    tcc = thermodynamics_dG_r_data();
                    tcc.calculate_dG0_r_v3(cobra_model, dG_f_data.measured_dG_f, dG_f_data.estimated_dG_f, other_data.temperature); # calculate the change in free energy of reaction without accounting for metabolite concentrations
                    tcc.calculate_dG_r_v3(cobra_model,metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations,
                                        other_data.pH, other_data.ionic_strength, other_data.temperature); # adjust the change in free energy of reaction for intracellular metabolite concentrations
                    tcc.check_thermodynamicConsistency(cobra_model,simulated_data.fva_data,
                                        metabolomics_data.measured_concentrations,
                                        metabolomics_data.estimated_concentrations,
                                        other_data.pH,other_data.ionic_strength,other_data.temperature,
                                        measured_concentration_coverage_criteria_I,
                                        measured_dG_f_coverage_criteria_I); # check the thermodynamic consistency of the data
                    tcc.calculate_displacement_v3(cobra_model,metabolomics_data.measured_concentrations, metabolomics_data.estimated_concentrations); # calculate the displacements from equillibrium
                    #tcc.simulate_infeasibleReactions(cobra_model); # simulate thermodynamically inconsistent data
                    #tcc.constrain_infeasibleReactions(cobra_model); # remove thermodynamically inconsistent reactions from the model
                    # upload dG0r, dGr, displacements, and results of tcc
                    for k,v in tcc.dG_r.items():
                        dG0_r_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'rxn_id':k,
                                'Keq_lb':tcc.dG0_r[k]['Keq_lb'],
                                'Keq_ub':tcc.dG0_r[k]['Keq_ub'],
                                'dG0_r':tcc.dG0_r[k]['dG_r'],
                                'dG0_r_var':tcc.dG0_r[k]['dG_r_var'],
                                'dG0_r_units':tcc.dG0_r[k]['dG_r_units'],
                                'dG0_r_lb':tcc.dG0_r[k]['dG_r_lb'],
                                'dG0_r_ub':tcc.dG0_r[k]['dG_r_ub'],
                                'used_':True,
                                'comment_':None};
                        dG0_r_O.append(dG0_r_tmp);
                        dG_r_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'rxn_id':k,
                                'Keq_lb':tcc.dG_r[k]['Keq_lb'],
                                'Keq_ub':tcc.dG_r[k]['Keq_ub'],
                                'dG_r':tcc.dG_r[k]['dG_r'],
                                'dG_r_var':tcc.dG_r[k]['dG_r_var'],
                                'dG_r_units':tcc.dG_r[k]['dG_r_units'],
                                'dG_r_lb':tcc.dG_r[k]['dG_r_lb'],
                                'dG_r_ub':tcc.dG_r[k]['dG_r_ub'],
                                'displacement_lb':tcc.displacement[k]['displacement_lb'],
                                'displacement_ub':tcc.displacement[k]['displacement_ub'],
                                'Q_lb':tcc.displacement[k]['Q_lb'],
                                'Q_ub':tcc.displacement[k]['Q_ub'],
                                'used_':True,
                                'comment_':None};
                        dG_r_O.append(dG_r_tmp);
                        tcc_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'rxn_id':k,
                                'feasible':tcc.thermodynamic_consistency_check[k],
                                'measured_concentration_coverage_criteria':measured_concentration_coverage_criteria_I,
                                'measured_dG_f_coverage_criteria':measured_dG_f_coverage_criteria_I,
                                'measured_concentration_coverage':tcc.metabolomics_coverage[k],
                                'measured_dG_f_coverage':tcc.dG_r_coverage[k],
                                'used_':True,
                                'comment_':None};
                        tcc_O.append(tcc_tmp);
                        #try:
                        #    row = None;
                        #    row = data_stage03_quantification_dG0_r(experiment_id_I,
                        #            model_id,
                        #            sna,
                        #            tp,
                        #            k,
                        #            tcc.dG0_r[k]['Keq_lb'],
                        #            tcc.dG0_r[k]['Keq_ub'],
                        #            tcc.dG0_r[k]['dG_r'],
                        #            tcc.dG0_r[k]['dG_r_var'],
                        #            tcc.dG0_r[k]['dG_r_units'],
                        #            tcc.dG0_r[k]['dG_r_lb'],
                        #            tcc.dG0_r[k]['dG_r_ub'],
                        #            True,
                        #            None);
                        #    self.session.add(row);
                        #    row = None;
                        #    row = data_stage03_quantification_dG_r(experiment_id_I,
                        #            model_id,
                        #            sna,
                        #            tp,
                        #            k,
                        #            tcc.dG_r[k]['Keq_lb'],
                        #            tcc.dG_r[k]['Keq_ub'],
                        #            tcc.dG_r[k]['dG_r'],
                        #            tcc.dG_r[k]['dG_r_var'],
                        #            tcc.dG_r[k]['dG_r_units'],
                        #            tcc.dG_r[k]['dG_r_lb'],
                        #            tcc.dG_r[k]['dG_r_ub'],
                        #            tcc.displacement[k]['displacement_lb'],
                        #            tcc.displacement[k]['displacement_ub'],
                        #            tcc.displacement[k]['Q_lb'],
                        #            tcc.displacement[k]['Q_ub'],
                        #            True,
                        #            None);
                        #    self.session.add(row);
                        #    row = None;
                        #    row = data_stage03_quantification_tcc(experiment_id_I,
                        #            model_id,
                        #            sna,
                        #            tp,
                        #            k,
                        #            tcc.thermodynamic_consistency_check[k],
                        #            measured_concentration_coverage_criteria_I,
                        #            measured_dG_f_coverage_criteria_I,
                        #            tcc.metabolomics_coverage[k],
                        #            tcc.dG_r_coverage[k],
                        #            True,
                        #            None);
                        #    self.session.add(row);
                        #except sqlalchemy.exc.IntegrityError as e:
                        #    print(e);
                        #    print("Press any key to continue")
                        #    a=input();
                    #self.session.commit();  
        # add datat to the DB
        self.add_dataStage03QuantificationDG0r(dG0_r_O);
        self.add_dataStage03QuantificationDGr(dG_r_O);
        self.add_dataStage03QuantificationTcc(tcc_O);
    def execute_simulateInfeasibleReactions(self,experiment_id_I,models_I,model_ids_I = [],
                            time_points_I=[],sample_name_abbreviations_I=[],constrain_infeasibleReactions_I=False):

        '''calculate dG0_r, dG_r, displacements, and perform a thermodynamic consistency check'''
        
        infeasible_reactions_O = [];
        # get the model ids:
        if model_ids_I:
            model_ids = model_ids_I;
        else:
            model_ids = [];
            model_ids = self.get_modelID_experimentID_dataStage03QuantificationSimulation(experiment_id_I);
        for model_id in model_ids:
            # get the cobra model
            cobra_model = models_I[model_id];
            # get the time-points
            if time_points_I:
                time_points = time_points_I;
            else:
                time_points = [];
                time_points = self.get_timePoints_experimentIDAndModelID_dataStage03QuantificationSimulation(experiment_id_I,model_id);
            for tp in time_points:
                # get sample_name_abbreviations
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndModelIDAndTimePoint_dataStage03QuantificationSimulation(experiment_id_I,model_id,tp);
                for sna in sample_name_abbreviations:
                    # get dG0_r and dG_r data
                    dG0_r={};
                    dG0_r=self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(experiment_id_I,model_id,tp,sna);
                    dG_r={};
                    dG_r=self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(experiment_id_I,model_id,tp,sna);
                    measured_concentration_coverage,measured_dG_f_coverage,feasible = {},{},{};
                    measured_concentration_coverage,measured_dG_f_coverage,feasible = self.get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(simulation_info['experiment_id'],simulation_info['model_id'],simulation_info['time_point'],simulation_info['sample_name_abbreviation'],0,0)
                    # load dG0r and dGr
                    tcc = thermodynamics_dG_r_data(dG0_r_I=dG0_r,dG_r_I=dG_r,
                         dG_r_coverage_I = measured_dG_f_coverage,
                         metabolomics_coverage_I = measured_concentration_coverage,
                         thermodynamic_consistency_check_I = feasible);
                    tcc.simulate_infeasibleReactions(cobra_model); # simulate thermodynamically inconsistent data
                    if constrain_infeasibleReactions_I:
                        tcc.constrain_infeasibleReactions(cobra_model); # remove thermodynamically inconsistent reactions from the model
                    # upload dG0r, dGr, displacements, and results of tcc
                    for k,v in tcc.dG_r.items():
                        tcc_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'rxn_id':k,
                                'feasible':tcc.thermodynamic_consistency_check[k],
                                'measured_concentration_coverage_criteria':measured_concentration_coverage_criteria_I,
                                'measured_dG_f_coverage_criteria':measured_dG_f_coverage_criteria_I,
                                'measured_concentration_coverage':tcc.metabolomics_coverage[k],
                                'measured_dG_f_coverage':tcc.dG_r_coverage[k],
                                'used_':True,
                                'comment_':None};
    
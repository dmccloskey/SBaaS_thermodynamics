# System
import json
# SBaaS
from .stage03_quantification_dG_r_query import stage03_quantification_dG_r_query
from .stage03_quantification_dG_r_dependencies import stage03_quantification_dG_r_dependencies
from .stage03_quantification_analysis_query import stage03_quantification_analysis_query
from .stage03_quantification_simulation_query import stage03_quantification_simulation_query
from .stage03_quantification_measuredData_query import stage03_quantification_measuredData_query
from SBaaS_models.models_escherMaps_query import models_escherMaps_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from molmass.molmass import Formula
import numpy
# Dependencies from escher
from escher import Builder

class stage03_quantification_dG_r_io(stage03_quantification_dG_r_query,
                                     stage03_quantification_dG_r_dependencies,
                                     stage03_quantification_analysis_query,
                                     stage03_quantification_simulation_query,
                                     stage03_quantification_measuredData_query,
                                     models_escherMaps_query):
            
    def import_dataStage03dG0r_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03dG0r(data.data);
        data.clear_data();

    def import_dataStage03dG0r_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03dG0r(data.data);
        data.clear_data();

    def import_dataStage03dGr_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03dGr(data.data);
        data.clear_data();

    def import_dataStage03dGr_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03dGr(data.data);
        data.clear_data();
            
    def import_dataStage03dGf_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03dGf(data.data);
        data.clear_data();

    def import_dataStage03tcc_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage03tcc(data.data);
        data.clear_data();

    def import_dataStage03tcc_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage03tcc(data.data);
        data.clear_data();

    def export_thermodynamicAnalysisEscher_js(self,analysis_id_I,simulation_id_I=None,
                     measured_concentration_coverage_criteria_I=0.49,
                     measured_dG_f_coverage_criteria_I=0.99,
                     data_dir_I = 'tmp'):
        
        data_O = [];
        # Get the simulation information
        if simulation_id_I:
            simulation_id = simulation_id_I;
        else:
            simulation_ids = [];
            simulation_ids = self.get_simulationID_analysisID_dataStage03QuantificationAnalysis(analysis_id_I);
        if not simulation_ids:
            print('No simulation found for the analysis_id ' + analysis_id_I);
        elif len(simulation_ids)>1:
            print('More than 1 simulation found for the analysis_id ' + analysis_id_I);
            simulation_id_I = simulation_ids[0];
        else:
            simulation_id_I = simulation_ids[0];
        # get the simulation info
        simulation = [];
        simulation = self.get_rows_simulationID_dataStage03QuantificationSimulation(simulation_id_I);
        for row in simulation:
            model_id = row['model_id'];
            # get the time-points
            tp = row['time_point'];
            # get the sample name abbreviations
            sna = row['sample_name_abbreviation'];
            # get the experiment
            experiment_id = row['experiment_id'];
            # get metabolomicsData
            concentrations = [];
            concentrations = self.get_rows_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(experiment_id,tp,sna);
            # get dGr
            dG_r = [];
            dG_r = self.get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(experiment_id,model_id,tp,sna,measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I);       
            if dG_r:
                for cnt,d in enumerate(dG_r):
                    dG_r[cnt]['dG_r_mean'] = numpy.mean([d['dG_r_lb'],d['dG_r_ub']]);
        # Get the map information
        map = [];
        map = self.get_rows_modelID_modelsEschermaps('iJO1366');

        # Make the ddt objects
        data1_keys = ['experiment_id',
                      #'model_id',
                      'time_point','sample_name_abbreviation','dG_r','dG_r_units'
                    ];
        data1_nestkeys = ['sample_name_abbreviation'];
        data1_keymap = {'values':'dG_r_mean','key':'rxn_id'};
        data2_keys = ['experiment_id','time_point',
                      'sample_name_abbreviation','met_id',
                      'concentration_units'
                    ];
        data2_nestkeys = ['sample_name_abbreviation'];
        data2_keymap = {'values':'concentration','key':'met_id'};
        data3_keys = ['model_id','eschermap_id'
                    ];
        data3_nestkeys = ['model_id'];
        data3_keymap = {'data':'eschermap_json'};
        # make the data object
        dataobject_O = [{"data":dG_r,"datakeys":data1_keys,"datanestkeys":data1_nestkeys},
                        {"data":concentrations,"datakeys":data2_keys,"datanestkeys":data2_nestkeys},
                        {"data":map,"datakeys":data3_keys,"datanestkeys":data3_nestkeys}];
        # make the tile parameter objects
        # form 1
        formtileparameters1_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters1_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters1_O.update(formparameters1_O);
        # form 2
        formtileparameters2_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu2",'rowid':"row1",'colid':"col2",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters2_O = {'htmlid':'filtermenuform2',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit2','text':'submit'},"formresetbuttonidtext":{'id':'reset2','text':'reset'},"formupdatebuttonidtext":{'id':'update2','text':'update'}};
        formtileparameters2_O.update(formparameters2_O);
        # form 3
        formtileparameters3_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu3",'rowid':"row2",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-6"};
        formparameters3_O = {'htmlid':'filtermenuform3',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit3','text':'submit'},"formresetbuttonidtext":{'id':'reset3','text':'reset'},"formupdatebuttonidtext":{'id':'update3','text':'update'}};
        formtileparameters3_O.update(formparameters3_O);
        # form 3
        # escher
        htmlparameters_O = {"htmlkeymap":[data1_keymap,data2_keymap],
                        'htmltype':'escher_01','htmlid':'html1',
                        'escherdataindex':{"reactiondata":0,"metabolitedata":1,"mapdata":2},
                        'escherembeddedcss':None,
                        'escheroptions':None};
        htmltileparameters_O = {'tileheader':'Escher map','tiletype':'html','tileid':"tile1",'rowid':"row3",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        htmltileparameters_O.update(htmlparameters_O);
        # table 1
        tableparameters1_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters1_O = {'tileheader':'dG_r','tiletype':'table','tileid':"table1",'rowid':"row4",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters1_O.update(tableparameters1_O);
        # table 2
        tableparameters2_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters2_O = {'tileheader':'Concentrations','tiletype':'table','tileid':"table2",'rowid':"row5",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters2_O.update(tableparameters2_O);
        # output objects
        parametersobject_O = [formtileparameters1_O,formtileparameters2_O,formtileparameters3_O,htmltileparameters_O,tabletileparameters1_O,tabletileparameters2_O];
        tile2datamap_O = {"filtermenu1":[0],"filtermenu2":[1],"filtermenu3":[2],"tile1":[0,1,2],"table1":[0],"table2":[1]};
        filtermenuobject_O = [{"filtermenuid":"filtermenu1","filtermenuhtmlid":"filtermenuform1",
                "filtermenusubmitbuttonid":"submit1","filtermenuresetbuttonid":"reset1",
                "filtermenuupdatebuttonid":"update1"},{"filtermenuid":"filtermenu2","filtermenuhtmlid":"filtermenuform2",
                "filtermenusubmitbuttonid":"submit2","filtermenuresetbuttonid":"reset2",
                "filtermenuupdatebuttonid":"update2"},{"filtermenuid":"filtermenu3","filtermenuhtmlid":"filtermenuform3",
                "filtermenusubmitbuttonid":"submit3","filtermenuresetbuttonid":"reset3",
                "filtermenuupdatebuttonid":"update3"}];
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        filtermenu_str = 'var ' + 'filtermenu' + ' = ' + json.dumps(filtermenuobject_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_export_thermodynamicAnalysisEscher' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str + '\n' + filtermenu_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
            file.write(filtermenu_str);

    def export_thermodynamicAnalysisComparison_csv(self,experiment_id_I,sample_name_abbreviation_base,
                    model_ids_I=[],
                    models_I={},
                     time_points_I=[],
                     sample_name_abbreviations_I=[],
                     measured_concentration_coverage_criteria_I=0.5,
                     measured_dG_f_coverage_criteria_I=0.99,
                     filename='tacomparison.csv'):
        '''export concentration and dG_r data for visualization'''
        
        # get the model ids:
        data_O = [];
        if model_ids_I:
            model_ids = model_ids_I;
        else:
            model_ids = [];
            model_ids = self.get_modelID_experimentID_dataStage03QuantificationSimulation(experiment_id_I);
        for model_id in model_ids:
            print('exporting thermodynamic analysis for model_id ' + model_id);
            # get the cobra model
            if models_I:
                cobra_model = models_I[model_id];
            else:
                cobra_model_sbml = None;
                cobra_model_sbml = self.get_row_modelID_dataStage02PhysiologyModels(model_id);
                # write the model to a temporary file
                with open('data/cobra_model_tmp.xml','w') as file:
                    file.write(cobra_model_sbml['model_file']);
                # Read in the sbml file and define the model conditions
                cobra_model = create_cobra_model_from_sbml_file('data/cobra_model_tmp.xml', print_time=True);
            # get the time-points
            if time_points_I:
                time_points = time_points_I;
            else:
                time_points = [];
                time_points = self.get_timePoints_experimentIDAndModelID_dataStage03QuantificationSimulation(experiment_id_I,model_id);
            for tp in time_points:
                print('exporting thermodynamic analysis for time_point ' + tp);
                # get sample_name_abbreviations
                if sample_name_abbreviations_I:
                    sample_name_abbreviations = sample_name_abbreviations_I;
                else:
                    sample_name_abbreviations = [];
                    sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndModelIDAndTimePoint_dataStage03QuantificationSimulation(experiment_id_I,model_id,tp);
                sample_name_abbreviations = [sna for sna in sample_name_abbreviations if sna !=sample_name_abbreviation_base]
                # get information about the sample to be compared
                concentrations_base = {};
                concentrations_base = self.get_rowsEscher_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(experiment_id_I,tp,sample_name_abbreviation_base);
                # get tcc
                tcc_base = [];
                tcc_base = self.get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(experiment_id_I,model_id,tp,sample_name_abbreviation_base,measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I);
                for sna in sample_name_abbreviations:
                    print('exporting thermodynamic analysis for sample_name_abbreviation ' + sample_name_abbreviation_base+'_vs_'+sna);
                    for tcc_b in tcc_base:
                        # get tcc
                        tcc = {};
                        tcc = self.get_row_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(experiment_id_I,model_id,tp,sna,tcc_b['rxn_id'],tcc_b['dG_r_lb'],tcc_b['dG_r_ub'],measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I);
                        # record data
                        if tcc:
                            # test for statistical and biological significance
                            significant_stat=self.check_significanceStatistical(tcc_b['dG_r_lb'],tcc_b['dG_r_ub'],tcc['dG_r_lb'],tcc['dG_r_ub']);
                            significant_bio=self.check_significanceBiological(tcc_b['dG_r_lb'],tcc_b['dG_r_ub'],tcc['dG_r_lb'],tcc['dG_r_ub']);
                            data_O.append({'experiment_id':experiment_id_I,
                            'model_id':model_id,
                            'sample_name_abbreviation':sna,
                            'time_point':tp,
                            'rxn_id':tcc['rxn_id'],
                            'dG_r_units':tcc['dG_r_units'],
                            'dG_r_lb_base':tcc_b['dG_r_lb'],
                            'dG_r_lb':tcc['dG_r_lb'],
                            'dG_r_ub_base':tcc_b['dG_r_ub'],
                            'dG_r_ub':tcc['dG_r_ub'],
                            'displacement_lb_base':tcc_b['displacement_lb'],
                            'displacement_lb':tcc['displacement_lb'],
                            'displacement_ub_base':tcc_b['displacement_ub'],
                            'displacement_ub':tcc['displacement_ub'],
                            'feasible_base':tcc_b['feasible'],
                            'feasible':tcc['feasible'],
                            'significant_stat':significant_stat,
                            'significant_bio':significant_bio});
        # write data to csv
        headers = ['experiment_id',
                            'model_id',
                            'sample_name_abbreviation',
                            'time_point',
                            'rxn_id',
                            'dG_r_units',
                            'dG_r_lb_base',
                            'dG_r_ub_base',
                            'dG_r_lb',
                            'dG_r_ub',
                            'displacement_lb_base',
                            'displacement_lb',
                            'displacement_ub_base',
                            'displacement_ub',
                            'feasible_base',
                            'feasible',
                            'significant_stat',
                            'significant_bio']
        io = base_exportData(data_O);
        filename_str = filename.split('.')[0] + experiment_id_I + '.' + filename.split('.')[1];
        io.write_dict2csv(filename_str,headers);

    def export_thermodynamicAnalysis_js(self,analysis_id_I,simulation_ids_I=[],
                     measured_concentration_coverage_criteria_I=0.49,
                     measured_dG_f_coverage_criteria_I=0.99,
                     bullet_chart_I = True,
                     data_dir_I = 'tmp'):
        '''Export the results of the thermodynamic analysis to js'''
        concentrations_O = [];
        dG_r_O = [];
        tcc_O = [];
        # Get the simulation information
        if simulation_ids_I:
            simulation_ids = simulation_ids_I;
        else:
            simulation_ids = [];
            simulation_ids = self.get_simulationID_analysisID_dataStage03QuantificationAnalysis(analysis_id_I);
        for simulation_id in simulation_ids:
            # get the simulation info
            simulation = [];
            simulation = self.get_rows_simulationID_dataStage03QuantificationSimulation(simulation_id);
            for row in simulation:
                model_id = row['model_id'];
                # get the time-points
                tp = row['time_point'];
                # get the sample name abbreviations
                sna = row['sample_name_abbreviation'];
                # get the experiment
                experiment_id = row['experiment_id'];
                ## get metabolomicsData
                #concentrations = [];
                #concentrations = self.get_rows_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(experiment_id_I,tp,sna);
                ## extend the data
                #concentrations_O.extend(concentrations);
                ## get dGr
                #dG_r = [];
                #dG_r = self.get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(experiment_id_I,model_id,tp,sna,measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I);       
                ## extend the data
                #dG_r_O.extend(dG_r);
                # get the tcc data
                tcc = [];
                tcc = self.get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(experiment_id,model_id,tp,sna,measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I);
                # record data
                if tcc: 
                    for cnt,d in enumerate(tcc):
                        tcc[cnt]['dG_r_mean'] = numpy.mean([d['dG_r_lb'],d['dG_r_ub']]);
                    tcc_O.extend(tcc);

        # dump chart parameters to a js files
        data1_keys = ['experiment_id',
                      'model_id',
                      'time_point','sample_name_abbreviation','rxn_id','dG_r_units','feasible'
                    ];
        data1_nestkeys = ['rxn_id'];
        if bullet_chart_I:
            data1_keymap = {'xdata':'rxn_id',
                        'ydata':'dG_r_mean',
                        'ydatalb':'dG_r_lb',
                        'ydataub':'dG_r_ub',
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'rxn_id'};
        else: # not implemented
            data1_keymap = {'xdata':'rxn_id',
                        'ydata':'dG_r_mean',
                        'ydatalb':'dG_r_lb',
                        'ydataub':'dG_r_ub',
                        'ydatamin':'min',
                        'ydatamax':'max',
                        'ydataiq1':'dG_r_lb_stdev',
                        'ydataiq3':'dG_r_ub_stdev',
                        'ydatamedian':'dG_r',
                        'serieslabel':'sample_name_abbreviation',
                        'featureslabel':'rxn_id'};
        # make the data object
        dataobject_O = [{"data":tcc_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys}];
        # make the tile parameter objects
        formtileparameters_O = {'tileheader':'Filter menu','tiletype':'html','tileid':"filtermenu1",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        formparameters_O = {'htmlid':'filtermenuform1',"htmltype":'form_01',"formsubmitbuttonidtext":{'id':'submit1','text':'submit'},"formresetbuttonidtext":{'id':'reset1','text':'reset'},"formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        svgparameters_O = {"svgtype":'boxandwhiskersplot2d_01',"svgkeymap":[data1_keymap,data1_keymap],
                            'svgid':'svg1',
                            "svgmargin":{ 'top': 50, 'right': 350, 'bottom': 50, 'left': 50 },
                            "svgwidth":750,"svgheight":350,
                            "svgx1axislabel":"rxn_id","svgy1axislabel":"dG_r",
    						'svgformtileid':'filtermenu1','svgresetbuttonid':'reset1','svgsubmitbuttonid':'submit1'};
        svgtileparameters_O = {'tileheader':'dG_r','tiletype':'svg','tileid':"tile2",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        svgtileparameters_O.update(svgparameters_O);
        tableparameters_O = {"tabletype":'responsivetable_01',
                    'tableid':'table1',
                    "tablefilters":None,
                    "tableclass":"table  table-condensed table-hover",
    			    'tableformtileid':'filtermenu1','tableresetbuttonid':'reset1','tablesubmitbuttonid':'submit1'};
        tabletileparameters_O = {'tileheader':'dG_r','tiletype':'table','tileid':"tile3",'rowid':"row1",'colid':"col1",
            'tileclass':"panel panel-default",'rowclass':"row",'colclass':"col-sm-12"};
        tabletileparameters_O.update(tableparameters_O);
        parametersobject_O = [formtileparameters_O,svgtileparameters_O,tabletileparameters_O];
        tile2datamap_O = {"filtermenu1":[0],"tile2":[0],"tile3":[0]};
        # dump the data to a json file
        data_str = 'var ' + 'data' + ' = ' + json.dumps(dataobject_O) + ';';
        parameters_str = 'var ' + 'parameters' + ' = ' + json.dumps(parametersobject_O) + ';';
        tile2datamap_str = 'var ' + 'tile2datamap' + ' = ' + json.dumps(tile2datamap_O) + ';';
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='project':
            filename_str = self.settings['visualization_data'] + '/project/' + analysis_id_I + '_data_stage02_isotopomer_fittedNetFluxes' + '.js'
        elif data_dir_I=='data_json':
            data_json_O = data_str + '\n' + parameters_str + '\n' + tile2datamap_str;
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(data_str);
            file.write(parameters_str);
            file.write(tile2datamap_str);
                
   
#SBaaS
from .stage03_quantification_dG_f_io import stage03_quantification_dG_f_io
from .stage03_quantification_otherData_query import stage03_quantification_otherData_query
from .stage03_quantification_metid2keggid_query import stage03_quantification_metid2keggid_query
from .stage03_quantification_simulation_query import stage03_quantification_simulation_query
# Dependencies from thermodynamics
from thermodynamics.thermodynamics_dG_f_data import thermodynamics_dG_f_data
from thermodynamics.thermodynamics_otherData import thermodynamics_otherData

class stage03_quantification_dG_f_execute(stage03_quantification_dG_f_io,
                                          stage03_quantification_otherData_query,
                                          stage03_quantification_metid2keggid_query,
                                          stage03_quantification_simulation_query):
    def execute_adjust_dG_f(self,experiment_id_I,models_I,model_ids_I = [],time_points_I=[],sample_name_abbreviations_I=[]):
        '''adjust dG0_f to specified temperature, pH, and ionic strength'''
        
        dGf_O = [];
        # query dG0f data
        id2kegg = {};
        id2kegg = self.get_rowsDict_dataStage03QuantificationMetid2keggid();
        dG0_f = {};
        dG0_f = self.get_rowsDict_dataStage03QuantificationDG0f();
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
                    # get otherData
                    pH,temperature,ionic_strength = {},{},{}
                    pH,temperature,ionic_strength = self.get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(experiment_id_I,tp,sna);
                    # load pH, ionic_strength, and temperature parameters
                    other_data = thermodynamics_otherData(pH_I=pH,temperature_I=temperature,ionic_strength_I=ionic_strength);
                    #other_data.load_defaultData();
                    other_data.check_data();
                    # adjust dG0f to environmental conditions
                    dG_f_data = thermodynamics_dG_f_data(id2KEGGID_I=id2kegg);
                    dG_f_data.get_transformed_dG_f(dG0_f,cobra_model,other_data.pH,other_data.temperature,other_data.ionic_strength); # adjust the non-transformed dG0_f data to physiological pH, temperature, and ionic strength (this step has already been completed)
                    # upload to database for later use
                    for k,v in dG_f_data.dG_f.items():
                        compartment = k.split('_')[-1]; #compartment id is appended to the met_id
                        data_tmp={'experiment_id':experiment_id_I,
                            'model_id':model_id,
                            'sample_name_abbreviation':sna,
                            'time_point':tp,
                            'met_name':None,
                            'met_id':k,
                            'dG_f':v['dG_f'],
                            'dG_f_var':v['dG_f_var'],
                            'dG_f_units':v['dG_f_units'],
                            'dG_f_lb':None,
                            'dG_f_ub':None,
                            'temperature':temperature[compartment]['temperature'],
                            'temperature_units':temperature[compartment]['temperature_units'],
                            'ionic_strength':ionic_strength[compartment]['ionic_strength'],
                            'ionic_strength_units':ionic_strength[compartment]['ionic_strength_units'],
                            'pH':pH[compartment]['pH'],
                            'pH_units':None,
                            'measured':True,
                            'used_':True,
                            'comment_':None};
                        dGf_O.append(data_tmp);
                        #row = None;
                        #row = data_stage03_quantification_dG_f(experiment_id_I,
                        #    model_id,
                        #    sna,
                        #    tp,
                        #    None,
                        #    k,
                        #    v['dG_f'],
                        #    v['dG_f_var'],
                        #    v['dG_f_units'],
                        #    None,
                        #    None,
                        #    temperature[compartment]['temperature'],
                        #    temperature[compartment]['temperature_units'],
                        #    ionic_strength[compartment]['ionic_strength'],
                        #    ionic_strength[compartment]['ionic_strength_units'],
                        #    pH[compartment]['pH'],
                        #    None,
                        #    True,
                        #    True,
                        #    None);
                        #self.session.add(row);
        #add data to to the DB
        self.add_dataStage03QuantificationDGf(dGf_O);
        #self.session.commit();
    
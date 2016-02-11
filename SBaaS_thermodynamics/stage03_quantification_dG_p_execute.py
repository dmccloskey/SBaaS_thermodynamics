#SBaaS
from .stage03_quantification_dG_p_io import stage03_quantification_dG_p_io
from .stage03_quantification_dG_r_query import stage03_quantification_dG_r_query
from .stage03_quantification_simulation_query import stage03_quantification_simulation_query
from SBaaS_models.models_COBRA_query import models_COBRA_query
#SBaaS models (delete if not needed)
from .stage03_quantification_dG_p_postgresql_models import *
# Resources (delete if not needed)
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
# Dependencies from thermodynamics
from thermodynamics.thermodynamics_dG_p_data import thermodynamics_dG_p_data
from thermodynamics.thermodynamics_dG_r_data import thermodynamics_dG_r_data

class stage03_quantification_dG_p_execute(stage03_quantification_dG_p_io,
                                          stage03_quantification_dG_r_query,
                                          stage03_quantification_simulation_query,
                                          models_COBRA_query):
    def execute_calculate_dG_p(self,experiment_id_I,models_I,model_ids_I = [],
                               time_points_I=[],sample_name_abbreviations_I=[]):
        '''calculate dG0_p and dG_p, and perform a thermodynamic consistency check'''
        
        # get the model ids:
        if model_ids_I:
            model_ids = model_ids_I;
        else:
            model_ids = [];
            model_ids = self.get_modelID_experimentID_dataStage03QuantificationSimulation(experiment_id_I);
        for model_id in model_ids:
            # get the cobra model
            cobra_model = models_I[model_id];
            # get pathway data
            pathways = {};
            pathways = self.get_rowsDict_modelID_dataStage02PhysiologyModelPathways(model_id);
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
                    # load dG0r and dGr
                    tcc = thermodynamics_dG_r_data(dG0_r_I=dG0_r,dG_r_I=dG_r);
                    # calculate dG_p for biosynthetic pathways
                    tccp = thermodynamics_dG_p_data(pathways_I=pathways);
                    tccp.calculate_dG_p(cobra_model,tcc.dG0_r,tcc.dG_r);
                    # upload dG_p
                    for k,v in tccp.dG_p.items():
                        dG0_p_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'pathway_id':k,
                                'dG0_p':tccp.dG0_p[k]['dG0_p'],
                                'dG0_p_var':tccp.dG0_p[k]['dG0_p_var'],
                                'dG0_p_units':tccp.dG0_p[k]['dG0_p_units'],
                                'dG0_p_lb':tccp.dG0_p[k]['dG0_p_lb'],
                                'dG0_p_ub':tccp.dG0_p[k]['dG0_p_ub'],
                                'used_':True,
                                'comment_':None};
                        dG_p_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'time_point':tp,
                                'pathway_id':k,
                                'dG_p':tccp.dG_p[k]['dG_p'],
                                'dG_p_var':tccp.dG_p[k]['dG_p_var'],
                                'dG_p_units':tccp.dG_p[k]['dG_p_units'],
                                'dG_p_lb':tccp.dG_p[k]['dG_p_lb'],
                                'dG_p_ub':tccp.dG_p[k]['dG_p_ub'],
                                'used_':True,
                                'comment_':None};
                        try:
                            row = None;
                            row = data_stage03_quantification_dG0_p(experiment_id_I,
                                    model_id,
                                    sna,
                                    tp,
                                    k,
                                    tccp.dG0_p[k]['dG0_p'],
                                    tccp.dG0_p[k]['dG0_p_var'],
                                    tccp.dG0_p[k]['dG0_p_units'],
                                    tccp.dG0_p[k]['dG0_p_lb'],
                                    tccp.dG0_p[k]['dG0_p_ub'],
                                    True,
                                    None);
                            self.session.add(row);
                            row = None;
                            row = data_stage03_quantification_dG_p(experiment_id_I,
                                    model_id,
                                    sna,
                                    tp,
                                    k,
                                    tccp.dG_p[k]['dG_p'],
                                    tccp.dG_p[k]['dG_p_var'],
                                    tccp.dG_p[k]['dG_p_units'],
                                    tccp.dG_p[k]['dG_p_lb'],
                                    tccp.dG_p[k]['dG_p_ub'],
                                    True,
                                    None);
                            self.session.add(row);
                        except sqlalchemy.exc.IntegrityError as e:
                            print(e);
                            print("Press any key to continue")
                            a=input();
                    self.session.commit();
    
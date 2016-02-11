#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS models
from .stage03_quantification_dG_p_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
#other

class stage03_quantification_dG_p_query(sbaas_base):

    def add_dataStage03dGp(self, data_I):
        '''add rows of data_stage03_quantification_dG_p'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_dG_p(d['experiment_id'],
                        d['model_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['pathway_id'],
                        d['dG_p'],
                        d['dG_p_var'],
                        d['dG_p_units'],
                        d['dG_p_lb'],
                        d['dG_p_ub'],
                        d['reactions'],
                        d['stoichiometry'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03dGp(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_dG_p'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG_p).filter(
                            data_stage03_quantification_dG_p.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'pathway_id':d['pathway_id'],
                            'dG_p':d['dG_p'],
                            'dG_p_var':d['dG_p_var'],
                            'dG_p_units':d['dG_p_units'],
                            'dG_p_lb':d['dG_p_lb'],
                            'dG_p_ub':d['dG_p_ub'],
                            'reactions':d['reactions'],
                            'stoichiometry':d['stoichiometry'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_dG_p(self):
        try:
            data_stage03_quantification_dG0_p.__table__.drop(self.engine,True);
            data_stage03_quantification_dG_p.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG_p(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_dG0_p).filter(data_stage03_quantification_dG0_p.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_dG_p).filter(data_stage03_quantification_dG_p.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_dG_p).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_dG0_p).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_dG_p(self):
        try:
            data_stage03_quantification_dG0_p.__table__.create(self.engine,True);
            data_stage03_quantification_dG_p.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
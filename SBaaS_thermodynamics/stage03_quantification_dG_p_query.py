#SBaaS models
from .stage03_quantification_dG_p_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#other

class stage03_quantification_dG_p_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_dG_p
        '''
        tables_supported = {'data_stage03_quantification_dG_p':data_stage03_quantification_dG_p,
            'data_stage03_quantification_dG0_p':data_stage03_quantification_dG0_p,
            };
        self.set_supportedTables(tables_supported);

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
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_dG_p(self):
        try:
            data_stage03_quantification_dG0_p.__table__.create(self.engine,True);
            data_stage03_quantification_dG_p.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
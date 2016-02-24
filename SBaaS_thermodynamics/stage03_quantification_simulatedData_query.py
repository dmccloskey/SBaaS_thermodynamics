#SBaaS models
from .stage03_quantification_simulatedData_postgresql_models import *
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

class stage03_quantification_simulatedData_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_simulatedData
        '''
        tables_supported = {'data_stage03_quantification_simulatedData':data_stage03_quantification_simulatedData,

            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_simulatedData
    # query rows from data_stage03_quantification_simulatedData    
    def get_rows_experimentIDAndModelID_dataStage03QuantificationSimulatedData(self,experiment_id_I,model_id_I):
        '''Query rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_simulatedData).filter(
                    data_stage03_quantification_simulatedData.model_id.like(model_id_I),
                    data_stage03_quantification_simulatedData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulatedData.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.experiment_id,
                        'model_id':d.model_id,
                        'rxn_id':d.rxn_id,
                        'fba_flux':d.fba_flux,
                        'fva_minimum':d.fva_minimum,
                        'fva_maximum':d.fva_maximum,
                        'flux_units':d.flux_units,
                        'sra_gr':d.sra_gr,
                        'sra_gr_ratio':d.sra_gr_ratio,
                        'used_':d.used_,
                        'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_experimentIDAndModelID_dataStage03QuantificationSimulatedData(self,experiment_id_I,model_id_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_simulatedData).filter(
                    data_stage03_quantification_simulatedData.model_id.like(model_id_I),
                    data_stage03_quantification_simulatedData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulatedData.used_.is_(True)).all();
            fva_data_O = {};
            sra_data_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in fva_data_O:
                        print('duplicate rxn_id found!');
                    else:
                        fva_data_O[d.rxn_id]={
                            'minimum':d.fva_minimum,
                            'maximum':d.fva_maximum};
                        sra_data_O[d.rxn_id]={'gr':d.sra_gr,
                            'gr_ratio':d.sra_gr_ratio};
            return fva_data_O,sra_data_O;
        except SQLAlchemyError as e:
            print(e);
    # update rows of data_stage03_quantification_simulatedData    
    def update_dataStage03QuantificationSimulatedData(self,data_I):
        '''update rows of data_stage03_quantification_simulatedData'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_simulatedData).filter(
                            data_stage03_quantification_simulatedData.experiment_id.like(d['experiment_id']),
                            data_stage03_quantification_simulatedData.model_id.like(d['model_id']),
                            data_stage03_quantification_simulatedData.rxn_id.like(d['rxn_id'])).update(
                            {
                            'fba_flux':d['fba_flux'],
                            'fva_minimum':d['fva_minimum'],
                            'fva_maximum':d['fva_maximum'],
                            'flux_units':d['flux_units'],
                            'sra_gr':d['sra_gr'],
                            'sra_gr_ratio':d['sra_gr_ratio'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03QuantificationSimulatedData(self, data_I):
        '''add rows of data_stage03_quantification_simulatedData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_simulatedData(d
                        #d['experiment_id'],
                        #d['model_id'],
                        #d['rxn_id'],
                        #d['fba_flux'],
                        #d['fva_minimum'],
                        #d['fva_maximum'],
                        #d['flux_units'],
                        #d['sra_gr'],
                        #d['sra_gr_ratio'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationSimulatedData(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_simulatedData'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_simulatedData).filter(
                            data_stage03_quantification_simulatedData.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'rxn_id':d['rxn_id'],
                            'fba_flux':d['fba_flux'],
                            'fva_minimum':d['fva_minimum'],
                            'fva_maximum':d['fva_maximum'],
                            'flux_units':d['flux_units'],
                            'sra_gr':d['sra_gr'],
                            'sra_gr_ratio':d['sra_gr_ratio'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_simulatedData(self):
        try:
            data_stage03_quantification_simulatedData.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_simulatedData(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_simulatedData).filter(data_stage03_quantification_simulatedData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_simulatedData).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_simulatedData(self):
        try:
            data_stage03_quantification_simulatedData.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
            
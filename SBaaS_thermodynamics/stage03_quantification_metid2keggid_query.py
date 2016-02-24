#SBaaS models
from .stage03_quantification_metid2keggid_postgresql_models import *
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

class stage03_quantification_metid2keggid_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_metid2keggid
        '''
        tables_supported = {'data_stage03_quantification_metid2keggid':data_stage03_quantification_metid2keggid,
            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_metid2keggid
    # query rows from data data_stage03_quantification_metid2keggid
    def get_rows_dataStage03QuantificationMetid2keggid(self):
        '''Querry rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_metid2keggid).filter(
                    data_stage03_quantification_metid2keggid.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {
                            'met_id':d.met_id,
                            'KEGG_ID':d.KEGG_id,
                            'used_':d.used_,
                            'comments_':d.comments_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsDict_dataStage03QuantificationMetid2keggid(self):
        '''Querry rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_metid2keggid).filter(
                    data_stage03_quantification_metid2keggid.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    row_tmp = {};
                    row_tmp[d.met_id] = d.KEGG_id;
                    rows_O.update(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03QuantificationMetid2keggid(self, data_I):
        '''add rows of data_stage03_quantification_metid2keggid'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_metid2keggid(d
                        #d['met_id'],
                        #d['KEGG_id'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationMetid2keggid(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_metid2keggid'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_metid2keggid).filter(
                            data_stage03_quantification_metid2keggid.id.like(d['id'])).update(
                            {
                            'met_id':d['met_id'],
                            'KEGG_id':d['KEGG_id'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_metid2keggid(self):
        try:
            data_stage03_quantification_metid2keggid.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_metid2keggid(self,met_id_I = None,simulation_id_I=None):
        try:
            if met_id_I:
                for met_id in met_id_I:
                    reset = self.session.query(data_stage03_quantification_metid2keggid).filter(data_stage03_quantification_metid2keggid.met_id.like(met_id)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_metid2keggid).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_metid2keggid(self):
        try:
            data_stage03_quantification_metid2keggid.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
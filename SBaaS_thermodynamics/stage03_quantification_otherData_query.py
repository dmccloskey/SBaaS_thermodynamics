#SBaaS models
from .stage03_quantification_otherData_postgresql_models import *
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

class stage03_quantification_otherData_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_otherData
        '''
        tables_supported = {'data_stage03_quantification_otherData':data_stage03_quantification_otherData,
            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_otherData
    # query rows from data data_stage03_quantification_otherData
    def get_rows_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage03_quantification_otherData).filter(
                    data_stage03_quantification_otherData.time_point.like(time_point_I),
                    data_stage03_quantification_otherData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_otherData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_otherData.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'compartment_id':d.compartment_id,
                            'pH':d.pH,
                            'temperature':d.temperature,
                            'temperature_units':d.temperature_units,
                            'ionic_strength':d.ionic_strength,
                            'ionic_strength_units':d.ionic_strength_units,
                            'used_':d.used_,
                            'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsFormatted_experimentIDAndTimePointAndSampleNameAbbreviation_dataStage03QuantificationOtherData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage03_quantification_otherData).filter(
                    data_stage03_quantification_otherData.time_point.like(time_point_I),
                    data_stage03_quantification_otherData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_otherData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_otherData.used_.is_(True)).all();
            pH_O = {};
            temperature_O = {};
            ionic_strength_O = {};
            if data: 
                for d in data:
                    pH_O[d.compartment_id]={'pH':d.pH};
                    temperature_O[d.compartment_id]={'temperature':d.temperature,
                            'temperature_units':d.temperature_units};
                    ionic_strength_O[d.compartment_id]={'ionic_strength':d.ionic_strength,
                            'ionic_strength_units':d.ionic_strength_units};
            return pH_O,temperature_O,ionic_strength_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03QuantificationOtherData(self, data_I):
        '''add rows of data_stage03_quantification_otherData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_otherData(d
                        #d['experiment_id'],
                        #d['sample_name_abbreviation'],
                        #d['time_point'],
                        #d['compartment_id'],
                        #d['pH'],
                        #d['temperature'],
                        #d['temperature_units'],
                        #d['ionic_strength'],
                        #d['ionic_strength_units'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationOtherData(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_otherData'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_otherData).filter(
                            data_stage03_quantification_otherData.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'compartment_id':d['compartment_id'],
                            'pH':d['pH'],
                            'temperature':d['temperature'],
                            'temperature_units':d['temperature_units'],
                            'ionic_strength':d['ionic_strength'],
                            'ionic_strength_units':d['ionic_strength_units'],
                            'used_':d['used_'],
                            'comment_I':d['comment_I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_otherData(self):
        try:
            data_stage03_quantification_otherData.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_otherData(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_otherData).filter(data_stage03_quantification_otherData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_otherData).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_otherData(self):
        try:
            data_stage03_quantification_otherData.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

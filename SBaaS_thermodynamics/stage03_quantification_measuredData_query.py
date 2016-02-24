#SBaaS models
from .stage03_quantification_measuredData_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage03_quantification_measuredData_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_measuredFluxes
        '''
        tables_supported = {'data_stage03_quantification_metabolomicsData':data_stage03_quantification_metabolomicsData,
            'data_stage03_quantification_measuredFluxes':data_stage03_quantification_measuredFluxes,
            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_metabolomicsData
    # query rows from data_stage03_quantification_metabolomicsData    
    def get_rows_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_metabolomicsData).filter(
                    data_stage03_quantification_metabolomicsData.time_point.like(time_point_I),
                    data_stage03_quantification_metabolomicsData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_metabolomicsData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_metabolomicsData.measured.is_(True),
                    data_stage03_quantification_metabolomicsData.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.experiment_id,
                        'sample_name_abbreviation':d.sample_name_abbreviation,
                        'time_point':d.time_point,
                        'met_id':d.met_id,
                        'concentration':d.concentration,
                        'concentration_var':d.concentration_var,
                        'concentration_units':d.concentration_units,
                        'concentration_lb':d.concentration_lb,
                        'concentration_ub':d.concentration_ub,
                        'measured':d.measured,
                        'used_':d.used_,
                        'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_metabolomicsData).filter(
                    data_stage03_quantification_metabolomicsData.time_point.like(time_point_I),
                    data_stage03_quantification_metabolomicsData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_metabolomicsData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_metabolomicsData.measured.is_(True),
                    data_stage03_quantification_metabolomicsData.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.met_id in rows_O:
                        print('duplicate met_ids found!');
                    else:
                        rows_O[d.met_id]={'concentration':d.concentration,
                            'concentration_var':d.concentration_var,
                            'concentration_units':d.concentration_units,
                            'concentration_lb':d.concentration_lb,
                            'concentration_ub':d.concentration_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherLbUb_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_metabolomicsData).filter(
                    data_stage03_quantification_metabolomicsData.time_point.like(time_point_I),
                    data_stage03_quantification_metabolomicsData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_metabolomicsData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_metabolomicsData.measured.is_(True),
                    data_stage03_quantification_metabolomicsData.used_.is_(True)).all();
            rows_O = [None,None];
            rows_O[0] = {};
            rows_O[1] = {}
            if data: 
                for d in data:
                    rows_O[0][d.met_id]=d.concentration_lb;
                    rows_O[1][d.met_id]=d.concentration_ub;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscher_experimentIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationMetabolomicsData(self,experiment_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_metabolomicsData).filter(
                    data_stage03_quantification_metabolomicsData.time_point.like(time_point_I),
                    data_stage03_quantification_metabolomicsData.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_metabolomicsData.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_metabolomicsData.measured.is_(True),
                    data_stage03_quantification_metabolomicsData.used_.is_(True)).all();
            rows_O = {}
            if data: 
                for d in data:
                    rows_O[d.met_id]=d.concentration;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
     
    ## Query from data_stage03_quantification_measuredFluxes
    # query rows from data_stage03_quantification_measuredFluxes
    def get_rows_experimentIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage03_quantification_measuredFluxes).filter(
                    data_stage03_quantification_measuredFluxes.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_measuredFluxes.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_measuredFluxes.used_.is_(True)).order_by(
                    data_stage03_quantification_measuredFluxes.model_id.asc(),
                    data_stage03_quantification_measuredFluxes.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                    'model_id':d.model_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    #'time_point':d.time_point,
                    'rxn_id':d.rxn_id,
                    'flux_average':d.flux_average,
                    'flux_stdev':d.flux_stdev,
                    'flux_lb':d.flux_lb,
                    'flux_ub':d.flux_ub,
                    'flux_units':d.flux_units,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationMeasuredFluxes(self,experiment_id_I,model_id_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage03_quantification_measuredFluxes).filter(
                    data_stage03_quantification_measuredFluxes.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_measuredFluxes.model_id.like(model_id_I),
                    data_stage03_quantification_measuredFluxes.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_measuredFluxes.used_.is_(True)).order_by(
                    data_stage03_quantification_measuredFluxes.model_id.asc(),
                    data_stage03_quantification_measuredFluxes.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                    'model_id':d.model_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    #'time_point':d.time_point,
                    'rxn_id':d.rxn_id,
                    'flux_average':d.flux_average,
                    'flux_stdev':d.flux_stdev,
                    'flux_lb':d.flux_lb,
                    'flux_ub':d.flux_ub,
                    'flux_units':d.flux_units,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_fluxDict_experimentIDAndModelIDAndSampleNameAbbreviationsAndTimePoint_dataStage03QuantificationMeasuredFluxes(self,experiment_id_I,model_id_I,sample_name_abbreviation_I,time_point_I):
        '''Query rows that are used from the measuredFluxes'''
        try:
            data = self.session.query(data_stage03_quantification_measuredFluxes).filter(
                    data_stage03_quantification_measuredFluxes.time_point.like(time_point_I),
                    data_stage03_quantification_measuredFluxes.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_measuredFluxes.model_id.like(model_id_I),
                    data_stage03_quantification_measuredFluxes.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_measuredFluxes.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in rows_O:
                        print('duplicate rxn_ids found!');
                    else:
                        rows_O[d.rxn_id]={'flux':d.flux_average,
                            'stdev':d.flux_stdev,
                            'units':d.flux_units,
                            'lb':d.flux_lb,
                            'ub':d.flux_ub,
                            'used_':d.used_,
                            'comment_':d.comment_};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03QuantificationMetabolomicsData(self, data_I):
        '''add rows of data_stage03_quantification_metabolomicsData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_metabolomicsData(d['experiment_id'],
                            d['sample_name_abbreviation'],
                            d['time_point'],
                            d['met_id'],
                            d['concentration'],
                            d['concentration_var'],
                            d['concentration_units'],
                            d['concentration_lb'],
                            d['concentration_ub'],
                            d['measured'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationMetabolomicsData(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_metabolomicsData'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_metabolomicsData).filter(
                            data_stage03_quantification_metabolomicsData.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'met_id':d['met_id'],
                            'concentration':d['concentration'],
                            'concentration_var':d['concentration_var'],
                            'concentration_units':d['concentration_units'],
                            'concentration_lb':d['concentration_lb'],
                            'concentration_ub':d['concentration_ub'],
                            'measured':d['measured'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def drop_dataStage03_quantification_measuredData(self):
        try:
            data_stage03_quantification_metabolomicsData.__table__.drop(self.engine,True);
            data_stage03_quantification_measuredFluxes.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_metabolomicsData(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_metabolomicsData).filter(data_stage03_quantification_metabolomicsData.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_metabolomicsData).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_measuredFluxes(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_measuredFluxes).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_measuredFluxes).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_measuredData(self):
        try:
            data_stage03_quantification_metabolomicsData.__table__.create(self.engine,True);
            data_stage03_quantification_measuredFluxes.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03QuantificationMeasuredFluxes(self, data_I):
        '''add rows of data_stage03_quantification_measuredFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_measuredFluxes(d['experiment_id'],
                            d['model_id'],
                            d['sample_name_abbreviation'],
                            d['time_point'],
                            d['rxn_id'],
                            d['flux_average'],
                            d['flux_stdev'],
                            d['flux_lb'],
                            d['flux_ub'],
                            d['flux_units'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_unique_dataStage03QuantificationMeasuredFluxes(self, data_I):
        '''update rows of data_stage03_quantification_measuredFluxes by unique columns
        '''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_measuredFluxes).filter(
                            data_stage03_quantification_measuredFluxes.experiment_id.like(d['experiment_id']),
                            data_stage03_quantification_measuredFluxes.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage03_quantification_measuredFluxes.time_point.like(d['time_point']),
                            data_stage03_quantification_measuredFluxes.rxn_id.like(d['rxn_id']),
                            data_stage03_quantification_measuredFluxes.flux_units.like(d['flux_units'])).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'flux_average':d['flux_average'],
                            'flux_stdev':d['flux_stdev'],
                            'flux_units':d['flux_units'],
                            'flux_lb':d['flux_lb'],
                            'flux_ub':d['flux_ub'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                    if data_update == 0:
                        print('row not found.')
                        print(d)
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
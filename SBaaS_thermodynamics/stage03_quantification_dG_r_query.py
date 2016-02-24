#SBaaS models
from .stage03_quantification_dG_r_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query
#Resources
#from math import copysign

class stage03_quantification_dG_r_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_dG_r
        '''
        tables_supported = {'data_stage03_quantification_dG0_r':data_stage03_quantification_dG0_r,
            'data_stage03_quantification_dG_r':data_stage03_quantification_dG_r,
            'data_stage03_quantification_tcc':data_stage03_quantification_tcc,
            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_dG0_r
    # query rows from data_stage03_quantificaton_dG0_r
    def get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDG0r(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_dG_f_coverage_criteria_I=0.0):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG0_r).filter(
                    data_stage03_quantification_dG0_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG0_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG0_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG0_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG0_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG0_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG0_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG0_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG0_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_dG0_r.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in rows_O:
                        print('duplicate rxn_id found!');
                    else:
                        rows_O[d.rxn_id]={
                        'Keq_lb':d.Keq_lb,
                        'Keq_ub':d.Keq_ub,
                        'dG_r':d.dG0_r,
                        'dG_r_var':d.dG0_r_var,
                        'dG_r_units':d.dG0_r_units,
                        'dG_r_lb':d.dG0_r_lb,
                        'dG_r_ub':d.dG0_r_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # update rows of data_stage03_quantification_dG0_r     
    def update_dataStage03DG0r(self,data_I):
        '''update rows of data_stage03_quantification_dG0_r'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG0_r).filter(
                            data_stage03_quantification_dG0_r.experiment_id.like(d['experiment_id']),
                            data_stage03_quantification_dG0_r.model_id.like(d['model_id']),
                            data_stage03_quantification_dG0_r.rxn_id.like(d['rxn_id']),
                            data_stage03_quantification_dG_r.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage03_quantification_dG_r.time_point.like(d['time_point'])).update(
                            {
                            'Keq_lb':d['Keq_lb'],
                            'Keq_ub':d['Keq_ub'],
                            'dG0_r':d['dG0_r'],
                            'dG0_r_var':d['dG0_r_var'],
                            'dG0_r_units':d['dG0_r_units'],
                            'dG0_r_lb':d['dG0_r_lb'],
                            'dG0_r_ub':d['dG0_r_ub'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    ## Query from data_stage03_quantification_dG_r
    # query rows from data_stage03_quantification_dG_r   
    def get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r).filter(
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True),
                    data_stage03_quantification_dG_r.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.experiment_id,
                        'model_id':d.model_id,
                        'sample_name_abbreviation':d.sample_name_abbreviation,
                        'time_point':d.time_point,
                        'rxn_id':d.rxn_id,
                        'Keq_lb':d.Keq_lb,
                        'Keq_ub':d.Keq_ub,
                        'dG_r':d.dG_r,
                        'dG_r_var':d.dG_r_var,
                        'dG_r_units':d.dG_r_units,
                        'dG_r_lb':d.dG_r_lb,
                        'dG_r_ub':d.dG_r_ub,
                        'displacement_lb':d.displacement_lb,
                        'displacement_ub':d.displacement_ub,
                        'Q_lb':d.Q_lb,
                        'Q_ub':d.Q_ub,
                        'used_':d.used_,
                        'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.0,
                                                                                                 measured_dG_f_coverage_criteria_I=0.0):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r).filter(
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_dG_r.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in rows_O:
                        print('duplicate rxn_id found!');
                    else:
                        rows_O[d.rxn_id]={
                        'Keq_lb':d.Keq_lb,
                        'Keq_ub':d.Keq_ub,
                        'dG_r':d.dG_r,
                        'dG_r_var':d.dG_r_var,
                        'dG_r_units':d.dG_r_units,
                        'dG_r_lb':d.dG_r_lb,
                        'dG_r_ub':d.dG_r_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherDGrLbUb_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r).filter(
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True),
                    data_stage03_quantification_dG_r.used_.is_(True)).all();
            rows_O = [None,None];
            rows_O[0] = {};
            rows_O[1] = {}
            if data: 
                for d in data:
                    rows_O[0][d.rxn_id]=d.dG_r_lb;
                    rows_O[1][d.rxn_id]=d.dG_r_ub;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherDGr_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGr(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r).filter(
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True),
                    data_stage03_quantification_dG_r.used_.is_(True)).all();
            rows_O = {}
            if data: 
                for d in data:
                    rows_O[d.rxn_id]=(d.dG_r_lb+d.dG_r_ub)/2;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # update rows of data_stage03_quantification_dG_r    
    def update_dataStage03DGr(self,data_I):
        '''update rows of data_stage03_quantification_dG_r'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG_r).filter(
                            data_stage03_quantification_dG_r.experiment_id.like(d['experiment_id']),
                            data_stage03_quantification_dG_r.model_id.like(d['model_id']),
                            data_stage03_quantification_dG_r.rxn_id.like(d['rxn_id']),
                            data_stage03_quantification_dG_r.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage03_quantification_dG_r.time_point.like(d['time_point'])).update(
                            {
                            'Keq_lb':d['Keq_lb'],
                            'Keq_ub':d['Keq_ub'],
                            'dG_r':d['dG_r'],
                            'dG_r_var':d['dG_r_var'],
                            'dG_r_units':d['dG_r_units'],
                            'dG_r_lb':d['dG_r_lb'],
                            'dG_r_ub':d['dG_r_ub'],
                            'displacement_lb':d['displacement_lb'],
                            'displacement_ub':d['displacement_ub'],
                            'Q_lb':d['Q_lb'],
                            'Q_ub':d['Q_ub'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    ## Query from data_stage03_quantification_tcc
    # query rows from data_stage03_quantification_tcc   
    def get_infeasibleReactions_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 feasible_I=False):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(
                data_stage03_quantification_tcc.rxn_id).filter(
                data_stage03_quantification_dG_r.model_id.like(model_id_I),
                data_stage03_quantification_dG_r.time_point.like(time_point_I),
                data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                data_stage03_quantification_tcc.feasible.is_(feasible_I),
                data_stage03_quantification_tcc.used_.is_(True),
                data_stage03_quantification_dG_r.used_.is_(True)).group_by(
                data_stage03_quantification_tcc.rxn_id).order_by(
                data_stage03_quantification_tcc.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.data_stage03_quantification_dG_r.experiment_id,
                        'model_id':d.data_stage03_quantification_dG_r.model_id,
                        'sample_name_abbreviation':d.data_stage03_quantification_dG_r.sample_name_abbreviation,
                        'time_point':d.data_stage03_quantification_dG_r.time_point,
                        'rxn_id':d.data_stage03_quantification_dG_r.rxn_id,
                        'dG_r_units':d.data_stage03_quantification_dG_r.dG_r_units,
                        'dG_r_lb':d.data_stage03_quantification_dG_r.dG_r_lb,
                        'dG_r_ub':d.data_stage03_quantification_dG_r.dG_r_ub,
                        'displacement_lb':d.data_stage03_quantification_dG_r.displacement_lb,
                        'displacement_ub':d.data_stage03_quantification_dG_r.displacement_ub,
                        'feasible':d.feasible,
                        'used_':d.data_stage03_quantification_dG_r.used_,
                        'comment_':d.data_stage03_quantification_dG_r.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);  
    # query rows from data_stage03_quantification_tcc   
    def get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the dG_r'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r,
                    data_stage03_quantification_tcc.measured_concentration_coverage,
                    data_stage03_quantification_tcc.measured_dG_f_coverage,
                    data_stage03_quantification_tcc.feasible).filter(
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True),
                    data_stage03_quantification_dG_r.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.data_stage03_quantification_dG_r.experiment_id,
                        'model_id':d.data_stage03_quantification_dG_r.model_id,
                        'sample_name_abbreviation':d.data_stage03_quantification_dG_r.sample_name_abbreviation,
                        'time_point':d.data_stage03_quantification_dG_r.time_point,
                        'rxn_id':d.data_stage03_quantification_dG_r.rxn_id,
                        'dG_r':d.data_stage03_quantification_dG_r.dG_r,
                        'dG_r_units':d.data_stage03_quantification_dG_r.dG_r_units,
                        'dG_r_lb':d.data_stage03_quantification_dG_r.dG_r_lb,
                        'dG_r_ub':d.data_stage03_quantification_dG_r.dG_r_ub,
                        'displacement_lb':d.data_stage03_quantification_dG_r.displacement_lb,
                        'displacement_ub':d.data_stage03_quantification_dG_r.displacement_ub,
                        'feasible':d.feasible,
                        'used_':d.data_stage03_quantification_dG_r.used_,
                        'comment_':d.data_stage03_quantification_dG_r.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);  
    def get_row_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                           rxn_id_I,
                                                                                                           dG_r_lb_I,
                                                                                                           dG_r_ub_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the dG_r
        Assumption: dG_r_lb < dG_r_ub'''
        try:
            data = self.session.query(data_stage03_quantification_dG_r,
                    data_stage03_quantification_tcc.measured_concentration_coverage,
                    data_stage03_quantification_tcc.measured_dG_f_coverage,
                    data_stage03_quantification_tcc.feasible).filter(
                    data_stage03_quantification_dG_r.rxn_id.like(rxn_id_I),
                    data_stage03_quantification_dG_r.model_id.like(model_id_I),
                    data_stage03_quantification_dG_r.time_point.like(time_point_I),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_r.model_id.like(data_stage03_quantification_tcc.model_id),
                    data_stage03_quantification_dG_r.time_point.like(data_stage03_quantification_tcc.time_point),
                    data_stage03_quantification_dG_r.sample_name_abbreviation.like(data_stage03_quantification_tcc.sample_name_abbreviation),
                    data_stage03_quantification_dG_r.experiment_id.like(data_stage03_quantification_tcc.experiment_id),
                    data_stage03_quantification_dG_r.rxn_id.like(data_stage03_quantification_tcc.rxn_id),
                    data_stage03_quantification_dG_r.used_.is_(True),
                    ## constraint for statistical significance
                    #or_(data_stage03_quantification_dG_r.dG_r_ub < dG_r_lb_I,
                    #    data_stage03_quantification_dG_r.dG_r_lb > dG_r_ub_I),
                    ## constraint for biological significance
                    #or_(copysign(1.0,data_stage03_quantification_dG_r.dG_r_lb) != copysign(1.0,dG_r_lb_I),
                    #    copysign(1.0,data_stage03_quantification_dG_r.dG_r_ub) != copysign(1.0,dG_r_ub_I)),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.data_stage03_quantification_dG_r.experiment_id,
                        'model_id':d.data_stage03_quantification_dG_r.model_id,
                        'sample_name_abbreviation':d.data_stage03_quantification_dG_r.sample_name_abbreviation,
                        'time_point':d.data_stage03_quantification_dG_r.time_point,
                        'rxn_id':d.data_stage03_quantification_dG_r.rxn_id,
                        'dG_r_units':d.data_stage03_quantification_dG_r.dG_r_units,
                        'dG_r_lb':d.data_stage03_quantification_dG_r.dG_r_lb,
                        'dG_r_ub':d.data_stage03_quantification_dG_r.dG_r_ub,
                        'displacement_lb':d.data_stage03_quantification_dG_r.displacement_lb,
                        'displacement_ub':d.data_stage03_quantification_dG_r.displacement_ub,
                        'feasible':d.feasible,
                        'used_':d.data_stage03_quantification_dG_r.used_,
                        'comment_':d.data_stage03_quantification_dG_r.comment_};
                    rows_O.update(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);  
        except TypeError as e:
            print(e);
    def get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationTCC(self,experiment_id_I,
                                                                                                           model_id_I,
                                                                                                           time_point_I,
                                                                                                           sample_name_abbreviation_I,
                                                                                                 measured_concentration_coverage_criteria_I=0.5,
                                                                                                 measured_dG_f_coverage_criteria_I=0.99):
        '''Query rows that are used from the tcc'''
        try:
            data = self.session.query(data_stage03_quantification_tcc.rxn_id,
                    data_stage03_quantification_tcc.measured_concentration_coverage,
                    data_stage03_quantification_tcc.measured_dG_f_coverage,
                    data_stage03_quantification_tcc.feasible).filter(
                    data_stage03_quantification_tcc.model_id.like(model_id_I),
                    data_stage03_quantification_tcc.time_point.like(time_point_I),
                    data_stage03_quantification_tcc.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_tcc.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_tcc.measured_concentration_coverage>measured_concentration_coverage_criteria_I,
                    data_stage03_quantification_tcc.measured_dG_f_coverage>measured_dG_f_coverage_criteria_I,
                    data_stage03_quantification_tcc.used_.is_(True)).all();
            measured_concentration_coverage_O = {};
            measured_dG_f_coverage_O = {};
            feasible_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in measured_concentration_coverage_O:
                        print('duplicate rxn_id found!');
                    else:
                        measured_concentration_coverage_O[d.rxn_id]={
                        'measured_concentration_coverage':d.measured_concentration_coverage
                        };
                        measured_dG_f_coverage_O[d.rxn_id]={
                        'measured_dG_f_coverage':d.measured_dG_f_coverage
                        };
                        feasible_O[d.rxn_id]={
                        'feasible':d.feasible
                        };
            return measured_concentration_coverage_O,measured_dG_f_coverage_O,feasible_O;
        except SQLAlchemyError as e:
            print(e);    
    # update rows of data_stage03_quantification_tcc  
    def update_dataStage03Tcc(self,data_I):
        '''update rows of data_stage03_quantification_tcc'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_tcc).filter(
                            data_stage03_quantification_tcc.experiment_id.like(d['experiment_id']),
                            data_stage03_quantification_tcc.model_id.like(d['model_id']),
                            data_stage03_quantification_tcc.rxn_id.like(d['rxn_id']),
                            data_stage03_quantification_dG_r.sample_name_abbreviation.like(d['sample_name_abbreviation']),
                            data_stage03_quantification_dG_r.time_point.like(d['time_point'])).update(
                            {
                            'feasible':d['feasible'],
                            'measured_concentration_coverage_criteria':d['measured_concentration_coverage_criteria'],
                            'measured_dG_f_coverage_criteria':d['measured_dG_f_coverage_criteria'],
                            'measured_concentration_coverage':d['measured_concentration_coverage'],
                            'measured_dG_f_coverage':d['measured_dG_f_coverage'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03dG0r(self, data_I):
        '''add rows of data_stage03_quantification_dG0_r'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_dG0_r(d['experiment_id'],
                        d['model_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['rxn_id'],
                        d['Keq_lb'],
                        d['Keq_ub'],
                        d['dG0_r'],
                        d['dG0_r_var'],
                        d['dG0_r_units'],
                        d['dG0_r_lb'],
                        d['dG0_r_ub'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03dG0r(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_dG0_r'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG0_r).filter(
                            standards.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'Keq_lb':d['Keq_lb'],
                            'Keq_ub':d['Keq_ub'],
                            'dG0_r':d['dG0_r'],
                            'dG0_r_var':d['dG0_r_var'],
                            'dG0_r_units':d['dG0_r_units'],
                            'dG0_r_lb':d['dG0_r_lb'],
                            'dG0_r_ub':d['dG0_r_ub'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03dGr(self, data_I):
        '''add rows of data_stage03_quantification_dG_r'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_dG_r(d['experiment_id'],
                        d['model_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['rxn_id'],
                        d['Keq_lb'],
                        d['Keq_ub'],
                        d['dG_r'],
                        d['dG_r_var'],
                        d['dG_r_units'],
                        d['dG_r_lb'],
                        d['dG_r_ub'],
                        d['displacement_lb'],
                        d['displacement_ub'],
                        d['Q_lb'],
                        d['Q_ub'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03dGr(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_dG_r'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG_r).filter(
                            standards.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'Keq_lb':d['Keq_lb'],
                            'Keq_ub':d['Keq_ub'],
                            'dG_r':d['dG_r'],
                            'dG_r_var':d['dG_r_var'],
                            'dG_r_units':d['dG_r_units'],
                            'dG_r_lb':d['dG_r_lb'],
                            'dG_r_ub':d['dG_r_ub'],
                            'displacement_lb':d['displacement_lb'],
                            'displacement_ub':d['displacement_ub'],
                            'Q_lb':d['Q_lb'],
                            'Q_ub':d['Q_ub'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03tcc(self, data_I):
        '''add rows of data_stage03_quantification_tcc'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_tcc(d['experiment_id'],
                    d['model_id'],
                    d['sample_name_abbreviation'],
                    d['time_point'],
                    d['rxn_id'],
                    d['feasible'],
                    d['measured_concentration_coverage_criteria'],
                    d['measured_dG_f_coverage_criteria'],
                    d['measured_concentration_coverage'],
                    d['measured_dG_f_coverage'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03tcc(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_tcc'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_tcc).filter(
                            standards.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'feasible':d['feasible'],
                            'measured_concentration_coverage_criteria':d['measured_concentration_coverage_criteria'],
                            'measured_dG_f_coverage_criteria':d['measured_dG_f_coverage_criteria'],
                            'measured_concentration_coverage':d['measured_concentration_coverage'],
                            'measured_dG_f_coverage':d['measured_dG_f_coverage'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_dG_r(self):
        try:
            data_stage03_quantification_dG0_r.__table__.drop(self.engine,True);
            data_stage03_quantification_dG_r.__table__.drop(self.engine,True);
            data_stage03_quantification_tcc.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG_r_all(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_dG0_r).filter(data_stage03_quantification_dG0_r.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_dG_r).filter(data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_tcc).filter(data_stage03_quantification_tcc.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_dG0_r).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_dG_r).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_tcc).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_dG_r(self):
        try:
            data_stage03_quantification_dG0_r.__table__.create(self.engine,True);
            data_stage03_quantification_dG_r.__table__.create(self.engine,True);
            data_stage03_quantification_tcc.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG0_r(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_dG0_r).filter(data_stage03_quantification_dG0_r.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG_r(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_dG_r).filter(data_stage03_quantification_dG_r.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_dG_r).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_tcc(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_tcc).filter(data_stage03_quantification_tcc.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_tcc).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

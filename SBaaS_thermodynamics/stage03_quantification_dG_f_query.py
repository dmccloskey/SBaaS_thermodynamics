#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS models
from .stage03_quantification_dG_f_postgresql_models import *
#SBaaS base
from SBaaS_base.sbaas_base import sbaas_base
#other

class stage03_quantification_dG_f_query(sbaas_base):
    ## Query from data_stage03_quantification_dG0_f
    # query rows from data data_stage03_quantification_dG0_f
    def get_rows_dataStage03QuantificationDG0f(self):
        '''Querry rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_dG0_f).filter(
                    data_stage03_quantification_dG0_f.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {
                            'reference_id':d.reference_id,
                            'met_name':d.met_name,
                            'met_id':d.met_id,
                            'KEGG_ID':d.KEGG_id,
                            'priority':d.priority,
                            'dG0_f':d.dG0_f,
                            'dG0_f_var':d.dG0_f_var,
                            'dG0_f_units':d.dG0_f_units,
                            'temperature':d.temperature,
                            'temperature_units':d.temperature_units,
                            'ionic_strength':d.ionic_strength,
                            'ionic_strength_units':d.ionic_strength_units,
                            'pH':d.pH,
                            'pH_units':d.pH_units,
                            'used_':d.used_,
                            'comments_':d.comments_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsDict_dataStage03QuantificationDG0f(self):
        '''Querry rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_dG0_f).filter(
                    data_stage03_quantification_dG0_f.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.KEGG_id in rows_O:
                        rows_O[d.KEGG_id].append({
                            'reference_id':d.reference_id,
                            'priority':d.priority,
                            'dG0_f':d.dG0_f,
                            'dG0_f_var':d.dG0_f_var,
                            'dG0_f_units':d.dG0_f_units});
                    else:
                        rows_O[d.KEGG_id] = [];
                        rows_O[d.KEGG_id].append({
                            'reference_id':d.reference_id,
                            'priority':d.priority,
                            'dG0_f':d.dG0_f,
                            'dG0_f_var':d.dG0_f_var,
                            'dG0_f_units':d.dG0_f_units});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    ## Query from data_stage03_quantification_dG_f
    # query rows from data_stage03_quantification_dG_f    
    def get_rows_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(self,experiment_id_I,model_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used'''
        try:
            data = self.session.query(data_stage03_quantification_dG_f).filter(
                    data_stage03_quantification_dG_f.model_id.like(model_id_I),
                    data_stage03_quantification_dG_f.time_point.like(time_point_I),
                    data_stage03_quantification_dG_f.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_f.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_f.measured.is_(True),
                    data_stage03_quantification_dG_f.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'experiment_id':d.experiment_id,
                    'model_id':d.model_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    'time_point':d.time_point,
                    'met_name':d.met_name,
                    'met_id':d.met_id,
                    'dG_f':d.dG_f,
                    'dG_f_var':d.dG_f_var,
                    'dG_f_units':d.dG_f_units,
                    'dG_f_lb':d.dG_f_lb,
                    'dG_f_ub':d.dG_f_ub,
                    'temperature':d.temperature,
                    'temperature_units':d.temperature_units,
                    'ionic_strength':d.ionic_strength,
                    'ionic_strength_units':d.ionic_strength_units,
                    'pH':d.pH,
                    'pH_units':d.pH_units,
                    'measured':d.measured,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_experimentIDAndModelIDAndTimePointAndSampleNameAbbreviations_dataStage03QuantificationDGf(self,experiment_id_I,model_id_I,time_point_I,sample_name_abbreviation_I):
        '''Query rows that are used from the metabolomicsData'''
        try:
            data = self.session.query(data_stage03_quantification_dG_f).filter(
                    data_stage03_quantification_dG_f.model_id.like(model_id_I),
                    data_stage03_quantification_dG_f.time_point.like(time_point_I),
                    data_stage03_quantification_dG_f.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_dG_f.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_dG_f.measured.is_(True),
                    data_stage03_quantification_dG_f.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.met_id in rows_O:
                        print('duplicate met_ids found!');
                    else:
                        rows_O[d.met_id]={'dG_f':d.dG_f,
                            'dG_f_var':d.dG_f_var,
                            'dG_f_units':d.dG_f_units,
                            'dG_f_lb':d.dG_f_lb,
                            'dG_f_ub':d.dG_f_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03dGf(self, data_I):
        '''add rows of data_stage03_quantification_dG_f'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_dG_f(d['experiment_id'],
                        d['model_id'],
                        d['sample_name_abbreviation'],
                        d['time_point'],
                        d['met_name'],
                        d['met_id'],
                        d['dG_f'],
                        d['dG_f_units'],
                        d['dG_f_lb'],
                        d['dG_f_ub'],
                        d['temperature'],
                        d['temperature_units'],
                        d['ionic_strength'],
                        d['ionic_strength_units'],
                        d['pH'],
                        d['pH_units'],
                        d['measured'],
                        d['used_'],
                        d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03dGf(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_dG_f'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG_f).filter(
                            standards.id.like(d['id'])).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'met_name':d['met_name'],
                            'met_id':d['met_id'],
                            'dG_f':d['dG_f'],
                            'dG_f_units':d['dG_f_units'],
                            'dG_f_lb':d['dG_f_lb'],
                            'dG_f_ub':d['dG_f_ub'],
                            'temperature':d['temperature'],
                            'temperature_units':d['temperature_units'],
                            'ionic_strength':d['ionic_strength'],
                            'ionic_strength_units':d['ionic_strength_units'],
                            'pH':d['pH'],
                            'pH_units':d['pH_units'],
                            'measured':d['measured'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03dG0f(self, data_I):
        '''add rows of data_stage03_quantification_dG0_f'''
        if data_I:
            #for d in data_I:
            #    try:
            #        data_add = data_stage03_quantification_dG0_f(d['reference_id'],
            #            d['met_name'],
            #            d['met_id'],
            #            d['KEGG_id'],
            #            d['priority'],
            #            d['dG0_f'],
            #            d['dG0_f_units'],
            #            d['temperature'],
            #            d['temperature_units'],
            #            d['ionic_strength'],
            #            d['ionic_strength_units'],
            #            d['pH'],
            #            d['pH_units'],
            #            d['used_'],
            #            d['comment_']);
            #        self.session.add(data_add);
            #    except SQLAlchemyError as e:
            #        print(e);
            for k,v in data_I.items():
                for d in v:
                    try:
                        data_add = data_stage03_quantification_dG0_f(d['source'],
                            None,
                            None,
                            k,
                            d['priority'],
                            d['dG0_f'],
                            d['dG0_f_var'],
                            d['dG0_f_units'],
                            298.15,
                            'K',
                            0.0,
                            'M',
                            0.0,
                            None,
                            True,
                            None);
                        self.session.add(data_add);
                    except SQLAlchemyError as e:
                        print(e);
            self.session.commit();

    def update_dataStage03dG0f(self,data_I):
        #Not yet tested
        '''update rows of data_stage03_quantification_dG0_f'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_dG0_f).filter(
                            data_stage03_quantification_dG0_f.id.like(d['id'])).update(
                            {'reference_id':d['reference_id'],
                            'met_name':d['met_name'],
                            'met_id':d['met_id'],
                            'KEGG_id':d['KEGG_id'],
                            'priority':d['priority'],
                            'dG0_f':d['dG0_f'],
                            'dG0_f_var':d['dG0_f_var'],
                            'dG0_f_units':d['dG0_f_units'],
                            'temperature':d['temperature'],
                            'temperature_units':d['temperature_units'],
                            'ionic_strength':d['ionic_strength'],
                            'ionic_strength_units':d['ionic_strength_units'],
                            'pH':d['pH'],
                            'pH_units':d['pH_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_dG_f(self):
        try:
            data_stage03_quantification_dG0_f.__table__.drop(self.engine,True);
            data_stage03_quantification_dG_f.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG0_f(self):
        try:
            reset = self.session.query(data_stage03_quantification_dG0_f).delete(synchronize_session=False);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_dG_f(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_dG_f).filter(data_stage03_quantification_dG_f.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage03_quantification_dG_f).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_dG_f(self):
        try:
            data_stage03_quantification_dG0_f.__table__.create(self.engine,True);
            data_stage03_quantification_dG_f.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
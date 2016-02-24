#SBaaS models
from .stage03_quantification_simulation_postgresql_models import *
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

class stage03_quantification_simulation_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for data_stage03_quantification_simulation
        '''
        tables_supported = {'data_stage03_quantification_simulation':data_stage03_quantification_simulation,
            'data_stage03_quantification_simulationParameters':data_stage03_quantification_simulationParameters,
            };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage03_quantification_simulation
    # query sample_name_abbreviations from data_stage03_quantification_simulation
    def get_sampleNameAbbreviations_experimentID_dataStage03QuantificationSimulation(self,experiment_id_I):
        '''Querry sample_name_abbreviations that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.sample_name_abbreviation).filter(
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation).order_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndModelID_dataStage03QuantificationSimulation(self,experiment_id_I,model_id_I):
        '''Querry sample_name_abbreviations that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.sample_name_abbreviation).filter(
                    data_stage03_quantification_simulation.model_id.like(model_id_I),
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation).order_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndModelIDAndTimePoint_dataStage03QuantificationSimulation(self,experiment_id_I,model_id_I,time_point_I):
        '''Querry sample_name_abbreviations that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.sample_name_abbreviation).filter(
                    data_stage03_quantification_simulation.model_id.like(model_id_I),
                    data_stage03_quantification_simulation.time_point.like(time_point_I),
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation).order_by(
                    data_stage03_quantification_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query time_points from data_stage03_quantification_simulation
    def get_timePoints_experimentIDAndModelID_dataStage03QuantificationSimulation(self,experiment_id_I,model_id_I):
        '''Querry time-points that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.time_point).filter(
                    data_stage03_quantification_simulation.model_id.like(model_id_I),
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.time_point).order_by(
                    data_stage03_quantification_simulation.time_point.asc()).all();
            time_points_O = [];
            if data: 
                for d in data:
                    time_points_O.append(d.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    def get_timePoints_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage03QuantificationSimulation(self,experiment_id_I,model_id_I,sna_I):
        '''Querry time-points that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.time_point).filter(
                    data_stage03_quantification_simulation.model_id.like(model_id_I),
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.sample_name_abbreviation.like(sna_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.time_point).order_by(
                    data_stage03_quantification_simulation.time_point.asc()).all();
            time_points_O = [];
            if data: 
                for d in data:
                    time_points_O.append(d.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query model_ids from data_stage03_quantification_simulation
    def get_modelID_experimentID_dataStage03QuantificationSimulation(self,experiment_id_I):
        '''Querry model_ids that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.model_id).filter(
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.model_id).order_by(
                    data_stage03_quantification_simulation.model_id.asc()).all();
            model_ids_O = [];
            if data: 
                for d in data:
                    model_ids_O.append(d.model_id);
            return model_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_modelID_experimentIDAndSampleNameAbbreviations_dataStage03QuantificationSimulation(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry model_ids for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage03_quantification_simulation.model_id).filter(
                    data_stage03_quantification_simulation.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage03_quantification_simulation.experiment_id.like(experiment_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).group_by(
                    data_stage03_quantification_simulation.model_id).order_by(
                    data_stage03_quantification_simulation.model_id.asc()).all();
            model_ids_O = [];
            if data: 
                for d in data:
                    model_ids_O.append(d.model_id);
            return model_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage03_quantification_simulation
    def get_rows_simulationID_dataStage03QuantificationSimulation(self,simulation_id_I):
        '''Querry rows that are used from the simulation'''
        try:
            data = self.session.query(data_stage03_quantification_simulation).filter(
                    data_stage03_quantification_simulation.simulation_id.like(simulation_id_I),
                    data_stage03_quantification_simulation.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append({
                            'simulation_id':d.simulation_id,
                            'experiment_id':d.experiment_id,
                            'model_id':d.model_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'simulation_type':d.simulation_type,
                            'used_':d.used_,
                            'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage03QuantificationSimulation(self, data_I):
        '''add rows of data_stage03_quantification_simulation'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_simulation(d
                        #d['simulation_id'],
                        #d['experiment_id'],
                        #d['model_id'],
                        #d['sample_name_abbreviation'],
                        #d['time_point'],
                        #d['simulation_type'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationSimulation(self,data_I):
        '''update rows of data_stage03_quantification_simulation'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_simulation).filter(
                            data_stage03_quantification_simulation.id.like(d['id'])).update(
                            {
                            'simulation_id':d['simulation_id'],
                            'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'simulation_type':d['simulation_type'],
                            'used_':d['used_'],
                            'comment_I':d['comment_I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def add_dataStage03QuantificationSimulationParameters(self, data_I):
        '''add rows of data_stage03_quantification_simulationParameters'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage03_quantification_simulationParameters(d
                        #d['simulation_id'],
                        ##None, #d['simulation_dateAndTime'],
                        #d['solver_id'],
                        #d['n_points'],
                        #d['n_steps'],
                        #d['max_time'],
                        #d['sampler_id'],
                        ##None,
                        ##None,
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage03QuantificationSimulationParameters(self,data_I):
        '''update rows of data_stage03_quantification_simulationParameters'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage03_quantification_simulationParameters).filter(
                            data_stage03_quantification_simulationParameters.id.like(d['id'])).update(
                            {'simulation_id':d['simulation_id'],
                             #'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'solver_id':d['solver_id'],
                            'n_points':d['n_points'],
                            'n_steps':d['n_steps'],
                             'max_time':d['max_time'],
                             'sampler_id':d['sampler_id'],
                             #'solve_time':d['solve_time'],
                             #'solve_time_units':d['solve_time_units'],
                            'used_':d['used_'],
                            'comment_I':d['comment_I']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def drop_dataStage03_quantification_simulation(self):
        try:
            data_stage03_quantification_simulation.__table__.drop(self.engine,True);
            data_stage03_quantification_simulationParameters.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage03_quantification_simulation(self,experiment_id_I = None,simulation_id_I=None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage03_quantification_simulation).filter(data_stage03_quantification_simulation.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            elif simulation_id_I:
                reset = self.session.query(data_stage03_quantification_simulation).filter(data_stage03_quantification_simulation.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage03_quantification_simulationParameters).filter(data_stage03_quantification_simulationParameters.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage03_quantification_simulation(self):
        try:
            data_stage03_quantification_simulation.__table__.create(self.engine,True);
            data_stage03_quantification_simulationParameters.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);

    ##  Query from data_stage03_quantification_simulationParameters
    # query rows from data_stage03_quantification_simulation
    def get_rows_simulationID_dataStage03QuantificationSimulationParameters(self,simulation_id_I):
        '''Querry rows that are used from the simulationParameters'''
        try:
            data = self.session.query(data_stage03_quantification_simulationParameters).filter(
                    data_stage03_quantification_simulationParameters.simulation_id.like(simulation_id_I),
                    data_stage03_quantification_simulationParameters.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append({
                            'simulation_id':d.simulation_id,
                            #'simulation_dateAndTime':d.simulation_dateAndTime,
                            'solver_id':d.solver_id,
                            'n_points':d.n_points,
                            'n_steps':d.n_steps,
                            'max_time':d.max_time,
                            'sampler_id':d.sampler_id,
                            #'solve_time':d.solve_time,
                            #'solve_time_units':d.solve_time_units,
                            'used_':d.used_,
                            'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
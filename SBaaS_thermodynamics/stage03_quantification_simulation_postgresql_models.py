#SBaaS base
from SBaaS_base.postgresql_orm_base import *
#TODO: add simulation_id and simulation_type
class data_stage03_quantification_simulation(Base):
    __tablename__ = 'data_stage03_quantification_simulation'
    id = Column(Integer, Sequence('data_stage03_quantification_simulation_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    simulation_type = Column(String(100)); # sampling, fva, sra, fba, fba-loopless, pfba, etc.
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','model_id','sample_name_abbreviation','time_point','simulation_type'),
            UniqueConstraint('simulation_id'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.simulation_type=row_dict_I['simulation_type'];
        self.comment_=row_dict_I['comment_'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.model_id=row_dict_I['model_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.time_point=row_dict_I['time_point'];
        self.used_=row_dict_I['used_'];

    def __set__row__(self,simulation_id_I,
                 experiment_id_I,
            model_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            simulation_type_I,
            used__I,
            comment__I):
        self.simulation_id=simulation_id_I
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.simulation_type=simulation_type_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
            'experiment_id':self.experiment_id,
            'model_id':self.model_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'simulation_type':self.simulation_type,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

#TODO: add table
class data_stage03_quantification_simulationParameters(Base):
    __tablename__ = 'data_stage03_quantification_simulationParameters'
    id = Column(Integer, Sequence('data_stage03_quantification_simulationParameters_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    #simulation_dateAndTime = Column(DateTime);
    solver_id = Column(String);
    n_points = Column(Integer); # sampling-specific
    n_steps = Column(Integer); # sampling-specific
    max_time = Column(Float); # sampling-specific
    sampler_id = Column(String); # sampling-specific; gpSampler (Matlab) opGpSampler (Python)
    #solve_time = Column(Float);
    #solve_time_units = Column(String);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('simulation_id'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.n_steps=row_dict_I['n_steps'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.solver_id=row_dict_I['solver_id'];
        self.n_points=row_dict_I['n_points'];
        self.max_time=row_dict_I['max_time'];
        self.sampler_id=row_dict_I['sampler_id'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,
                 simulation_id_I,
        #simulation_dateAndTime_I,
        solver_id_I,
        n_points_I,
        n_steps_I,
        max_time_I,
        sampler_id_I,
        #solve_time_I,
        #solve_time_units_I,
        used__I,comment__I):
        self.simulation_id=simulation_id_I
        #self.simulation_dateAndTime=simulation_dateAndTime_I
        self.solver_id=solver_id_I
        self.n_points=n_points_I
        self.n_steps=n_steps_I
        self.max_time=max_time_I
        self.sampler_id=sampler_id_I
        #self.solve_time=solve_time_I
        #self.solve_time_units=solve_time_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
            #'simulation_dateAndTime':self.simulation_dateAndTime,
            'solver_id':self.solver_id,
            'n_points':self.n_points,
            'n_steps':self.n_steps,
            'max_time':self.max_time,
            'sampler_id':self.sampler_id,
            #'solve_time':self.solve_time,
            #'solve_time_units':self.solve_time_units,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
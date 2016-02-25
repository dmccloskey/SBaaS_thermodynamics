#SBaaS base
from SBaaS_base.postgresql_orm_base import *


class data_stage03_quantification_sampledPoints(Base):
    __tablename__ = 'data_stage03_quantification_sampledPoints'
    id = Column(Integer, Sequence('data_stage03_quantification_sampledData_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #sample_name_abbreviation = Column(String(100))
    mixed_fraction = Column(Float);
    data_dir = Column(String(500)); #
    infeasible_loops = Column(postgresql.ARRAY(String));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('simulation_id','simulation_dateAndTime'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.data_dir=row_dict_I['data_dir'];
        self.infeasible_loops=row_dict_I['infeasible_loops'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.mixed_fraction=row_dict_I['mixed_fraction'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,model_id_I,
        #    sample_name_abbreviation_I,
            mixed_fraction_I,data_dir_I,infeasible_loops_I,
                 used__I,comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        self.mixed_fraction=mixed_fraction_I
        self.data_dir=data_dir_I
        self.infeasible_loops=infeasible_loops_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        #'experiment_id':self.experiment_id,
        #        'model_id':self.model_id,
        #    'sample_name_abbreviation':self.sample_name_abbreviation,
                'data_dir':self.data_dir,
                'infeasible_loops':self.infeasible_loops,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_sampledData(Base):
    __tablename__ = 'data_stage03_quantification_sampledData'
    id = Column(Integer, Sequence('data_stage03_quantification_sampledData_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #sample_name_abbreviation = Column(String(100))
    variable_id = Column(String(100))
    variable_type = Column(String(50)) # e.g., flux, concentration, dG_r
    variable_units = Column(String(50), default = 'mmol*gDW-1*hr-1'); 
    sampling_points = Column(postgresql.ARRAY(Float)); #
    sampling_n = Column(Integer);
    sampling_ave = Column(Float);
    sampling_var = Column(Float);
    sampling_lb = Column(Float);
    sampling_ub = Column(Float);
    sampling_ci = Column(Float, default = 0.95);
    sampling_min = Column(Float);
    sampling_max = Column(Float);
    sampling_median = Column(Float);
    sampling_iq_1 = Column(Float);
    sampling_iq_3 = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('simulation_id','variable_id','variable_type'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.variable_id=row_dict_I['variable_id'];
        self.variable_type=row_dict_I['variable_type'];
        self.variable_units=row_dict_I['variable_units'];
        self.sampling_n=row_dict_I['sampling_n'];
        self.sampling_points=row_dict_I['sampling_points'];
        self.sampling_ave=row_dict_I['sampling_ave'];
        self.sampling_var=row_dict_I['sampling_var'];
        self.sampling_lb=row_dict_I['sampling_lb'];
        self.sampling_ub=row_dict_I['sampling_ub'];
        self.sampling_ci=row_dict_I['sampling_ci'];
        self.sampling_min=row_dict_I['sampling_min'];
        self.sampling_max=row_dict_I['sampling_max'];
        self.sampling_median=row_dict_I['sampling_median'];
        self.sampling_iq_1=row_dict_I['sampling_iq_1'];
        self.sampling_iq_3=row_dict_I['sampling_iq_3'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,model_id_I,
        #    sample_name_abbreviation_I,
            variable_id_I,variable_type_I,variable_units_I,
            sampling_points_I,sampling_n_I,
                 sampling_ave_I,sampling_var_I,sampling_lb_I,sampling_ub_I,
                 sampling_ci_I,
                 sampling_min_I,sampling_max_I,sampling_median_I,
                 sampling_iq_1_I,sampling_iq_3_I,
                 used__I,comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        self.variable_id=variable_id_I
        self.variable_type=variable_type_I
        self.variable_units=variable_units_I
        self.sampling_points=sampling_points_I
        self.sampling_n=sampling_n_I
        self.sampling_ave=sampling_ave_I
        self.sampling_var=sampling_var_I
        self.sampling_lb=sampling_lb_I
        self.sampling_ub=sampling_ub_I
        self.sampling_ci=sampling_ci_I
        self.sampling_min=sampling_min_I
        self.sampling_max=sampling_max_I
        self.sampling_median=sampling_median_I
        self.sampling_iq_1=sampling_iq_1_I
        self.sampling_iq_3=sampling_iq_3_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        #'experiment_id':self.experiment_id,
        #        'model_id':self.model_id,
        #    'sample_name_abbreviation':self.sample_name_abbreviation,
                'variable_id':self.variable_id,
                'variable_type':self.variable_type,
                'variable_units':self.variable_units,
                'sampling_points':self.sampling_points,
                'sampling_n':self.sampling_n,
                'sampling_ave':self.sampling_ave,
                'sampling_var':self.sampling_var,
                'sampling_lb':self.sampling_lb,
                'sampling_ub':self.sampling_ub,
                'sampling_ci':self.sampling_ci,
                'sampling_max':self.sampling_max,
                'sampling_min':self.sampling_min,
                'sampling_median':self.sampling_median,
                'sampling_iq_1':self.sampling_iq_1,
                'sampling_iq_3':self.sampling_iq_3,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
#TODO:
class data_stage03_quantification_tfbaReactions(Base):
    __tablename__ = 'data_stage03_quantification_tfbaReactions'
    id = Column(Integer, Sequence('data_stage03_quantification_tfbaReactions_id_seq'), primary_key=True)
    experiment_id = Column(String(50), primary_key=True)
    model_id = Column(String(50), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    rxn_id = Column(String(100), primary_key=True)
    flux_units = Column(String(50), default = 'mmol*gDW-1*hr-1');
    tfba_flux = Column(Float);
    tfva_flux_minimum = Column(Float);
    tfva_flux_maximum = Column(Float);
    tsampling_flux_average = Column(Float);
    tsampling_flux_var = Column(Float);
    dG_r_units = Column(Float);
    tfba_dG_r = Column(Float);
    tfva_dG_r_lb = Column(Float);
    tfva_dG_r_ub = Column(Float);
    tsampling_dG_r_average = Column(Float);
    tsampling_dG_r_var = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);
    
    def __init__(self, 
                row_dict_I,
                ):
        pass;
    def __set__row__(self,experiment_id_I):
        self.experiment_id=experiment_id_I

    def __repr__dict__(self):
        return {}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage03_quantification_tfbaMetabolites(Base):
    __tablename__ = 'data_stage03_quantification_tfbaMetabolites'
    id = Column(Integer, Sequence('data_stage03_quantification_tfbaMetabolites_id_seq'), primary_key=True)
    experiment_id = Column(String(100), primary_key=True)
    sample_name_abbreviation = Column(String(100), primary_key=True)
    time_point = Column(String(10), primary_key=True)
    met_id = Column(String(100), primary_key=True)
    concentration_units = Column(String(50));
    tfba_concentration_lb = Column(Float);
    tfva_concentration_lb = Column(Float);
    tfva_concentration_ub = Column(Float);
    tsampling_concentration_average = Column(Float);
    tsampling_concentration_var = Column(Float);
    dG_f_units = Column(Float);
    tfba_dG_f = Column(Float);
    tfva_dG_f_lb = Column(Float);
    tfva_dG_f_ub = Column(Float);
    tsampling_dG_f_average = Column(Float);
    tsampling_dG_f_var = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);
    
    def __init__(self, 
                row_dict_I,
                ):
        pass;
    def __set__row__(self, experiment_id_I):
        self.experiment_id = experiment_id_I;

    def __repr__dict__(self): 
        return {}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())


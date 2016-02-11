#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_dG0_r(Base):
    __tablename__ = 'data_stage03_quantification_dG0_r'
    id = Column(Integer, Sequence('data_stage03_quantification_dG0_r_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    rxn_id = Column(String(100))
    Keq_lb = Column(Float)
    Keq_ub = Column(Float)
    dG0_r = Column(Float);
    dG0_r_var = Column(Float);
    dG0_r_units = Column(String(50));
    dG0_r_lb = Column(Float);
    dG0_r_ub = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','model_id','sample_name_abbreviation','time_point','rxn_id'),
            )

    def __init__(self,experiment_id_I,model_id_I,sample_name_abbreviation_I,
                 time_point_I,rxn_id_I,Keq_lb_I,Keq_ub_I,
                 dG0_r_I,dG0_r_var_I,dG0_r_units_I,dG0_r_lb_I,
                 dG0_r_ub_I,used_I,comment_I):
        self.experiment_id = experiment_id_I;
        self.model_id = model_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.rxn_id = rxn_id_I;
        self.Keq_lb = Keq_lb_I;
        self.Keq_ub = Keq_ub_I;
        self.dG0_r = dG0_r_I;
        self.dG0_r_var = dG0_r_var_I;
        self.dG0_r_units = dG0_r_units_I;
        self.dG0_r_lb = dG0_r_lb_I;
        self.dG0_r_ub = dG0_r_ub_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'sample_type':self.sample_type,
                'time_point':self.time_point,
                'rxn_id':self.rxn_id,
                'Keq_lb':self.Keq_lb,
                'Keq_ub':self.Keq_ub,
                'dG0_r':self.dG0_r,
                'dG0_r_var':self.dG0_r_var,
                'dG0_r_units':self.dG0_r_units,
                'dG0_r_lb':self.dG0_r_lb,
                'dG0_r_ub':self.dG0_r_ub,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_dG_r(Base):
    __tablename__ = 'data_stage03_quantification_dG_r'
    id = Column(Integer, Sequence('data_stage03_quantification_dG_r_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    rxn_id = Column(String(100))
    Keq_lb = Column(Float)
    Keq_ub = Column(Float)
    dG_r = Column(Float);
    dG_r_var = Column(Float);
    dG_r_units = Column(String(50));
    dG_r_lb = Column(Float);
    dG_r_ub = Column(Float);
    displacement_lb = Column(Float);
    displacement_ub = Column(Float);
    Q_lb = Column(Float);
    Q_ub = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','model_id','sample_name_abbreviation','time_point','rxn_id'),
            )

    def __init__(self,experiment_id_I,
                    model_id_I,
                    sample_name_abbreviation_I,
                    time_point_I,
                    rxn_id_I,
                    Keq_lb_I,
                    Keq_ub_I,
                    dG_r_I,
                    dG_r_var_I,
                    dG_r_units_I,
                    dG_r_lb_I,
                    dG_r_ub_I,
                    displacement_lb_I,
                    displacement_ub_I,
                    Q_lb_I,
                    Q_ub_I,
                    used__I,
                    comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.Keq_lb = Keq_lb_I;
        self.Keq_ub = Keq_ub_I;
        self.dG_r=dG_r_I
        self.dG_r_var=dG_r_var_I
        self.dG_r_units=dG_r_units_I
        self.dG_r_lb=dG_r_lb_I
        self.dG_r_ub=dG_r_ub_I
        self.displacement_lb=displacement_lb_I
        self.displacement_ub=displacement_ub_I
        self.Q_lb=Q_lb_I
        self.Q_ub=Q_ub_I
        self.used_=used__I
        self.comment_=comment__I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'rxn_id':self.rxn_id,
                'Keq_lb':self.Keq_lb,
                'Keq_ub':self.Keq_ub,
                'dG_r':self.dG_r,
                'dG_r_var':self.dG_r_var,
                'dG_r_units':self.dG_r_units,
                'dG_r_lb':self.dG_r_lb,
                'dG_r_ub':self.dG_r_ub,
                'displacement_lb':self.displacement_lb,
                'displacement_ub':self.displacement_ub,
                'Q_lb':self.Q_lb,
                'Q_ub':self.Q_ub,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_tcc(Base):
    __tablename__ = 'data_stage03_quantification_tcc'
    id = Column(Integer, Sequence('data_stage03_quantification_tcc_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    rxn_id = Column(String(100))
    feasible = Column(Boolean);
    measured_concentration_coverage_criteria = Column(Float, default = 0.5);
    measured_dG_f_coverage_criteria = Column(Float, default = 0.99);
    measured_concentration_coverage = Column(Float);
    measured_dG_f_coverage = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','rxn_id'),
            )

    def __init__(self,experiment_id_I, model_id_I,sample_name_abbreviation_I,
                time_point_I,rxn_id_I,feasible_I,
                measured_concentration_coverage_criteria_I,measured_dG_f_coverage_criteria_I,
                measured_concentration_coverage_I,measured_dG_f_coverage_I,
                used__I,comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.feasible=feasible_I
        self.measured_concentration_coverage_criteria=measured_concentration_coverage_criteria_I
        self.measured_dG_f_coverage_criteria=measured_dG_f_coverage_criteria_I
        self.measured_concentration_coverage=measured_concentration_coverage_I
        self.measured_dG_f_coverage=measured_dG_f_coverage_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
            'model_id':self.model_id,
            'sample_name_abbreviation':self.sample_name_abbreviation,
            'time_point':self.time_point,
            'rxn_id':self.rxn_id,
            'feasible':self.feasible,
            'measured_concentration_coverage_criteria':self.measured_concentration_coverage_criteria,
            'measured_dG_f_coverage_criteria':self.measured_dG_f_coverage_criteria,
            'measured_concentration_coverage':self.measured_concentration_coverage,
            'measured_dG_f_coverage':self.measured_dG_f_coverage,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
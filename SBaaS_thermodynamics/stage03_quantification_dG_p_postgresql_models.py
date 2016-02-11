#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_dG_p(Base):
    __tablename__ = 'data_stage03_quantification_dG_p'
    id = Column(Integer, Sequence('data_stage03_quantification_dG_p_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    pathway_id = Column(String(100))
    dG_p = Column(Float);
    dG_p_var = Column(Float);
    dG_p_units = Column(String(50));
    dG_p_lb = Column(Float);
    dG_p_ub = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','pathway_id'),
            )

    def __init__(self,experiment_id_I,model_id_I,sample_name_abbreviation_I,
                 time_point_I,pathway_id_I,
                 dG_p_I,dG_p_var_I,dG_p_units_I,dG_p_lb_I,
                 dG_p_ub_I,used_I,comment_I,):
        self.experiment_id = experiment_id_I;
        self.model_id = model_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.pathway_id = pathway_id_I;
        self.dG_p = dG_p_I;
        self.dG_p_var = dG_p_var_I;
        self.dG_p_units = dG_p_units_I;
        self.dG_p_lb = dG_p_lb_I;
        self.dG_p_ub = dG_p_ub_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'pathway_id':self.pathway_id,
                'dG_p':self.dG_p,
                'dG_p_var':self.dG_p_var,
                'dG_p_units':self.dG_p_units,
                'dG_p_lb':self.dG_p_lb,
                'dG_p_ub':self.dG_p_ub,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_dG0_p(Base):
    __tablename__ = 'data_stage03_quantification_dG0_p'
    id = Column(Integer, Sequence('data_stage03_quantification_dG0_p_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    pathway_id = Column(String(100))
    dG0_p = Column(Float);
    dG0_p_var = Column(Float);
    dG0_p_units = Column(String(50));
    dG0_p_lb = Column(Float);
    dG0_p_ub = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','pathway_id'),
            )

    def __init__(self,experiment_id_I,model_id_I,sample_name_abbreviation_I,
                 time_point_I,pathway_id_I,
                 dG0_p_I,dG0_p_var_I,dG0_p_units_I,dG0_p_lb_I,
                 dG0_p_ub_I,used_I,comment_I,):
        self.experiment_id = experiment_id_I;
        self.model_id = model_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.pathway_id = pathway_id_I;
        self.dG0_p = dG0_p_I;
        self.dG0_p_var = dG0_p_var_I;
        self.dG0_p_units = dG0_p_units_I;
        self.dG0_p_lb = dG0_p_lb_I;
        self.dG0_p_ub = dG0_p_ub_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'pathway_id':self.pathway_id,
                'dG0_p':self.dG0_p,
                'dG0_p_var':self.dG0_p_var,
                'dG0_p_units':self.dG0_p_units,
                'dG0_p_lb':self.dG0_p_lb,
                'dG0_p_ub':self.dG0_p_ub,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
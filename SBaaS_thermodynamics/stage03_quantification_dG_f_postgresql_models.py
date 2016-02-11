#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_dG0_f(Base):
    __tablename__ = 'data_stage03_quantification_dG0_f'
    id = Column(Integer, Sequence('data_stage03_quantification_dG0_f_id_seq'), primary_key=True)
    reference_id = Column(String(100))
    met_name = Column(String(500))
    met_id = Column(String(100))
    KEGG_id = Column(String(20))
    priority = Column(Integer);
    dG0_f = Column(Float);
    dG0_f_var = Column(Float);
    dG0_f_units = Column(String(50));
    temperature = Column(Float, default=298.15);
    temperature_units = Column(String(50), default='K');
    ionic_strength = Column(Float, default=0.0);
    ionic_strength_units = Column(String(50),default='M');
    pH = Column(Float, default=0.0);
    pH_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('reference_id','KEGG_id','priority'),
            )

    def __init__(self, reference_id_I, met_name_I, met_id_I, KEGG_id_I, priority_I,
                 dG0_f_I, dG0_f_var_I, dG0_f_units_I, temperature_I, temperature_units_I, ionic_strength_I, ionic_strength_units_I,
                 pH_I, pH_units_I, used_I, comment_I):
        self.reference_id = reference_id_I;
        self.met_name = met_name_I;
        self.met_id = met_id_I;
        self.KEGG_id = KEGG_id_I;
        self.priority = priority_I;
        self.dG0_f = dG0_f_I;
        self.dG0_f_var = dG0_f_var_I;
        self.dG0_f_units = dG0_f_units_I;
        self.temperature = temperature_I;
        self.temperature_units = temperature_units_I;
        self.ionic_strength = ionic_strength_I;
        self.ionic_strength_units = ionic_strength_units_I;
        self.pH = pH_I;
        self.pH_units = pH_units_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'reference_id':self.reference_id,
                'met_name':self.met_name,
                'met_id':self.met_id,
                'KEGG_ID':self.KEGG_id,
                'priority':self.priority,
                'dG0_f':self.dG0_f,
                'dG0_f_var':self.dG0_f_var,
                'dG0_f_units':self.dG0_f_units,
                'temperature':self.temperature,
                'temperature_units':self.temperature_units,
                'ionic_strength':self.ionic_strength,
                'ionic_strength_units':self.ionic_strength_units,
                'pH':self.pH,
                'pH_units':self.pH_units,
                'used_':self.used_,
                'comments_':self.comments_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_dG_f(Base):
    __tablename__ = 'data_stage03_quantification_dG_f'
    id = Column(Integer, Sequence('data_stage03_quantification_dG_f_id_seq'), primary_key=True)
    experiment_id = Column(String(100))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    met_name = Column(String(500))
    met_id = Column(String(100))
    dG_f = Column(Float);
    dG_f_var = Column(Float);
    dG_f_units = Column(String(50));
    dG_f_lb = Column(Float);
    dG_f_ub = Column(Float);
    temperature = Column(Float);
    temperature_units = Column(String(50));
    ionic_strength = Column(Float);
    ionic_strength_units = Column(String(50));
    pH = Column(Float);
    pH_units = Column(String(50));
    measured = Column(Boolean);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','model_id','sample_name_abbreviation','time_point','met_id'),
            )

    def __init__(self, experiment_id_I,model_id_I,sample_name_abbreviation_I,
                 time_point_I, met_name_I, met_id_I,
                 dG_f_I, dG_f_var_I, dG_f_units_I, 
                 dG_f_lb_I, dG_f_ub_I, temperature_I, temperature_units_I,
                 ionic_strength_I, ionic_strength_units_I,
                 pH_I, pH_units_I, measured_I, used_I, comment_I):
        self.experiment_id = experiment_id_I;
        self.model_id = model_id_I;
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.met_name = met_name_I;
        self.met_id = met_id_I;
        self.dG_f = dG_f_I;
        self.dG_f_var = dG_f_var_I;
        self.dG_f_units = dG_f_units_I;
        self.dG_f_lb = dG_f_lb_I;
        self.dG_f_ub = dG_f_ub_I;
        self.temperature = temperature_I;
        self.temperature_units = temperature_units_I;
        self.ionic_strength = ionic_strength_I;
        self.ionic_strength_units = ionic_strength_units_I;
        self.pH = pH_I;
        self.pH_units = pH_units_I;
        self.measured = measured_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self): 
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                    'sample_name_abbreviation':self.sample_name_abbreviation,
                    'time_point':self.time_point,
                    'met_name':self.met_name,
                    'met_id':self.met_id,
                    'dG_f':self.dG_f,
                    'dG_f_var':self.dG_f_var,
                    'dG_f_units':self.dG_f_units,
                    'dG_f_lb':self.dG_f_lb,
                    'dG_f_ub':self.dG_f_ub,
                    'temperature':self.temperature,
                    'temperature_units':self.temperature_units,
                    'ionic_strength':self.ionic_strength,
                    'ionic_strength_units':self.ionic_strength_units,
                    'pH':self.pH,
                    'pH_units':self.pH_units,
                    'measured':self.measured,
                    'used_':self.used_,
                    'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
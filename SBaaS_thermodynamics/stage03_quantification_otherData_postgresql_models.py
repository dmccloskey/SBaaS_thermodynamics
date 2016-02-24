#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_otherData(Base):
    __tablename__ = 'data_stage03_quantification_otherData'
    id = Column(Integer, Sequence('data_stage03_quantification_otherData_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    compartment_id = Column(String(25))
    pH = Column(Float);
    temperature = Column(Float);
    temperature_units = Column(String(50));
    ionic_strength = Column(Float);
    ionic_strength_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','sample_name_abbreviation','compartment_id'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.comment_=data_dict_I['comment_'];
        self.experiment_id=data_dict_I['experiment_id'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.time_point=data_dict_I['time_point'];
        self.compartment_id=data_dict_I['compartment_id'];
        self.pH=data_dict_I['pH'];
        self.temperature=data_dict_I['temperature'];
        self.temperature_units=data_dict_I['temperature_units'];
        self.ionic_strength=data_dict_I['ionic_strength'];
        self.ionic_strength_units=data_dict_I['ionic_strength_units'];
        self.used_=data_dict_I['used_'];

    def __set__row__(self,experiment_id_I,sample_name_abbreviation_I,
                 time_point_I,compartment_id_I,pH_I,
                 temperature_I,temperature_units_I,ionic_strength_I,
                 ionic_strength_units_I,used__I,comment__I):
        self.experiment_id=experiment_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.compartment_id=compartment_id_I
        self.pH=pH_I
        self.temperature=temperature_I
        self.temperature_units=temperature_units_I
        self.ionic_strength=ionic_strength_I
        self.ionic_strength_units=ionic_strength_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'compartment_id':self.compartment_id,
                'pH':self.pH,
                'temperature':self.temperature,
                'temperature_units':self.temperature_units,
                'ionic_strength':self.ionic_strength,
                'ionic_strength_units':self.ionic_strength_units,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
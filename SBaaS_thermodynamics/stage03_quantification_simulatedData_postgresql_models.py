#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_simulatedData(Base):
    __tablename__ = 'data_stage03_quantification_simulatedData'
    id = Column(Integer, Sequence('data_stage03_quantification_simulatedData_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    fba_flux = Column(Float);
    fva_minimum = Column(Float);
    fva_maximum = Column(Float);
    flux_units = Column(String(50), default = 'mmol*gDW-1*hr-1');
    sra_gr = Column(Float);
    sra_gr_ratio = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('experiment_id','model_id','rxn_id'),
            )

    def __init__(self,experiment_id_I,model_id_I,
                 #sample_name_abbreviation_I,
                 #time_point_I,
                 rxn_id_I,fba_flux_I,
                 fva_minimum_I,fva_maximum_I,flux_units_I,
                 sra_gr_I,sra_gr_ratio_I,used__I,comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.fba_flux=fba_flux_I
        self.fva_minimum=fva_minimum_I
        self.fva_maximum=fva_maximum_I
        self.flux_units=flux_units_I
        self.sra_gr=sra_gr_I
        self.sra_gr_ratio=sra_gr_ratio_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'model_id':self.model_id,
                #'sample_name_abbreviation':self.sample_name_abbreviation,
                #'time_point':self.time_point,
                'rxn_id':self.rxn_id,
                'fba_flux':self.fba_flux,
                'fva_minimum':self.fva_minimum,
                'fva_maximum':self.fva_maximum,
                'flux_units':self.flux_units,
                'sra_gr':self.sra_gr,
                'sra_gr_ratio':self.sra_gr_ratio,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
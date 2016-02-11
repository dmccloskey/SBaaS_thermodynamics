from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_analysis(Base):
    __tablename__ = 'data_stage03_quantification_analysis'
    id = Column(Integer, Sequence('data_stage03_quantification_analysis_id_seq'), primary_key=True)
    analysis_id = Column(String(500))
    simulation_id = Column(String(500))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('analysis_id','simulation_id'),
            )

    def __init__(self,
            analysis_id_I,
            simulation_id_I,
            used__I,
            comment__I):
        self.analysis_id=analysis_id_I
        self.simulation_id=simulation_id_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
            'analysis_id':self.analysis_id,
            'simulation_id':self.simulation_id,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())


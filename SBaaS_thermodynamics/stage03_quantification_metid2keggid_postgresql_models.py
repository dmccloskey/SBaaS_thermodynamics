#SBaaS base
from SBaaS_base.postgresql_orm_base import *
    
class data_stage03_quantification_metid2keggid(Base):
    __tablename__ = 'data_stage03_quantification_metid2keggid'
    id = Column(Integer, Sequence('data_stage03_quantification_metid2keggid_id_seq'))
    met_id = Column(String(100))
    KEGG_id = Column(String(20), primary_key=True)
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('id'),
            )

    def __init__(self, met_id_I, KEGG_id_I, used_I, comment_I):
        self.met_id = met_id_I;
        self.KEGG_id = KEGG_id_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self): # not complete!
        return {'id':self.id,
                'met_id':self.met_id,
                'KEGG_ID':self.KEGG_id,
                'used_':self.used_,
                'comments_':self.comments_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
#SBaaS base
from SBaaS_base.postgresql_orm_base import *
class data_stage03_quantification_models(Base):
    __tablename__ = 'data_stage03_quantification_models'
    id = Column(Integer, Sequence('data_stage03_quantification_models_id_seq'),primary_key=True)
    model_id = Column(String(50))
    model_name = Column(String(100))
    model_description = Column(String(100))
    model_file = Column(Text)
    file_type = Column(String(50))
    date = Column(DateTime)

    __table_args__ = (
            UniqueConstraint('model_id'),
            )

    def __init__(self,model_id_I,
            model_name_I,
            model_description_I,
            model_file_I,
            file_type_I,
            date_I):
        self.model_id=model_id_I
        self.model_name=model_name_I
        self.model_description=model_description_I
        self.model_file=model_file_I
        self.file_type=file_type_I
        self.date=date_I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
                'model_name':self.model_name,
                'model_description':self.model_description,
                'model_file':self.model_file,
                'file_type':self.file_type,
                'date':self.date}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_modelReactions(Base):
    __tablename__ = 'data_stage03_quantification_modelReactions'
    id = Column(Integer, Sequence('data_stage03_quantification_modelReactions_id_seq'))
    model_id = Column(String(50), primary_key=True)
    rxn_id = Column(String(50), primary_key=True)
    rxn_name = Column(String(255))
    equation = Column(String(4000));
    subsystem = Column(String(255));
    gpr = Column(Text);
    genes = Column(postgresql.ARRAY(String(50)));
    reactants_stoichiometry = Column(postgresql.ARRAY(Float)) # stoichiometry of metabolites
    products_stoichiometry = Column(postgresql.ARRAY(Float)) 
    reactants_ids = Column(postgresql.ARRAY(String(50))) # list of met_ids that are in the reaction
    products_ids = Column(postgresql.ARRAY(String(50))) 
    lower_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    upper_bound = Column(Float) #derived from experimentally measured values or estimations from simulations
    objective_coefficient = Column(Float)
    flux_units = Column(String(50))
    reversibility = Column(Boolean)
    used_ = Column(Boolean)
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('id'),
            )

    def __init__(self,model_id_I,
            rxn_id_I,
            rxn_name_I,
            equation_I,
            subsystem_I,
            gpr_I,
            genes_I,
            reactants_stoichiometry_I,
            products_stoichiometry_I,
            reactants_ids_I,
            products_ids_I,
            lower_bound_I,
            upper_bound_I,
            objective_coefficient_I,
            flux_units_I,
            reversibility_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.rxn_id=rxn_id_I
        self.rxn_name=rxn_name_I
        self.equation=equation_I
        self.subsystem=subsystem_I
        self.gpr=gpr_I
        self.genes=genes_I
        self.reactants_stoichiometry=reactants_stoichiometry_I
        self.products_stoichiometry=products_stoichiometry_I
        self.reactants_ids=reactants_ids_I
        self.products_ids=products_ids_I
        self.lower_bound=lower_bound_I
        self.upper_bound=upper_bound_I
        self.objective_coefficient=objective_coefficient_I
        self.reversibility=reversibility_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
            'rxn_id':self.rxn_id,
            'rxn_name':self.rxn_name,
            'equation':self.equation,
            'subsystem':self.subsystem,
            'gpr':self.gpr,
            'genes':self.genes,
            'reactants_stoichiometry':self.reactants_stoichiometry,
            'products_stoichiometry':self.products_stoichiometry,
            'reactants_ids':self.reactants_ids,
            'products_ids':self.products_ids,
            'lower_bound':self.lower_bound,
            'upper_bound':self.upper_bound,
            'objective_coefficient':self.objective_coefficient,
            'flux_units':self.flux_units,
            'reversibility':self.reversibility,
            'used_':self.used_,
            'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage03_quantification_modelMetabolites(Base):
    __tablename__ = 'data_stage03_quantification_modelMetabolites'
    id = Column(Integer, Sequence('data_stage03_quantification_modelMetabolites_id_seq'))
    model_id = Column(String(50), primary_key=True)
    met_name = Column(String(500))
    met_id = Column(String(50), primary_key=True)
    formula = Column(String(100))
    charge = Column(Integer)
    compartment = Column(String(50))
    bound = Column(Float)
    constraint_sense = Column(String(5))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('id'),
            )

    def __init__(self,model_id_I,
            met_name_I,
            met_id_I,
            formula_I,
            charge_I,
            compartment_I,
            bound_I,
            constraint_sense_I,
            used__I,
            comment__I):
        self.model_id=model_id_I
        self.met_name=met_name_I
        self.met_id=met_id_I
        self.formula=formula_I
        self.charge=charge_I
        self.compartment=compartment_I
        self.bound=bound_I
        self.constraint_sense=constraint_sense_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
                'met_name':self.met_name,
                'met_id':self.met_id,
                'formula':self.formula,
                'charge':self.charge,
                'bound':self.bound,
                'constraint_sense':self.constraint_sense,
                'compartment':self.compartment,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage03_quantification_modelPathways(Base):
    __tablename__ = 'data_stage03_quantification_modelPathways'
    id = Column(Integer, Sequence('data_stage03_quantification_modelPathways_id_seq'))
    model_id = Column(String(50), primary_key=True)
    pathway_id = Column(String(100), primary_key=True)
    reactions = Column(postgresql.ARRAY(String(100)))
    stoichiometry = Column(postgresql.ARRAY(Float))
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (UniqueConstraint('id'),
            )

    def __init__(self,model_id_I,pathway_id_I,
                 reactions_I,stoichiometry_I,used_I,comment_I,):
        self.model_id = model_id_I;
        self.pathway_id = pathway_id_I;
        self.reactions = reactions_I;
        self.stoichiometry = stoichiometry_I;
        self.used_ = used_I;
        self.comment_ = comment_I;

    def __repr__dict__(self):
        return {'id':self.id,
                'model_id':self.model_id,
                'pathway_id':self.pathway_id,
                'reactions':self.reactions,
                'stoichiometry':self.stoichiometry,
                'used_':self.used_,
                'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
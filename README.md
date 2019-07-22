Création d’un module sous Odoo 


Partie 1 :
1. Crée le module « gestion_formation » avec les coordonnées suivantes :
 	• Nom : Gestion des formations.
 	• Version : 1.0
 	• Catégorie : formations.
 	• Auteur : votre_nom.
 	• Dépendances : {project}.
 	• Description : Ce module est destiné pour gérer un centre de formation.
Réponses: Il faut modifier le fichier __manifest__.py qui contient les paramètres de base

{
    'name': "Gestion des formations",

    'description': """
        Ce module est destiné pour gérer un centre de formation
    """,

    'author': "EL MOUSSAOUI Mohamed",

    # Categories can be used to filter modules in modules listing
    'category': 'Formations',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
}


2. Implémenté les classes et ces attributs dans le module.

Repense : Tout d’abord on import les classes dans models/__init__.py et on les créé :
Fichier models/__init__.py :

from . import candidat
from . import formateur
from . import formation
from . import salle
from . import session


Fichier models/candidat .py :

from odoo import models, fields, api
class Candidat(models.Model):
    _name = 'candidat.candidat'
    _description = 'Candidat description'
    
    name = fields.Char()
    num_ins = fields.Integer()


Fichier models/formateur.py :
class Formateur(models.Model):
    _name = 'formateur.formateur'
    _description = 'Formateur description'
    
    name = fields.Char()
    matricule = fields.Integer()
    diplome = fields.Char()


Fichier models/formation.py : 
class Formation(models.Model):
    _name = 'formation.formation'
    _description = 'Formation description'

    name = fields.Char()
    prix = fields.Float()


Fichier models/salle .py :
class Salle(models.Model):
    _name = 'salle.salle'
    _description = 'salle description'
    
    name = fields.Char()
    nb_place = fields.Integer()
    libre = fields.Boolean()


Fichier models/session .py :
class Session(models.Model):
    _name = 'session.session'
    _description = 'session description'

    name = fields.Char()
    nb_participants = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char()
    state = fields.Selection([])



3. Crée pour chaque objet une interface contenant les menus, les actions, et les vues
(form & tree & search & kanban pour les formateurs et les candidats).

Interface Formation :
    <!-- view_formation_form-->
    <record id="view_formation_form" model="ir.ui.view">
            <field name="name">formation.formation.form</field>
            <field name="model">formation.formation</field>
            <field name="priority" eval="8" />
            <fielpourd name="arch" type="xml">
                <form string="formation">
                    <sheet>
                        <div class="oe_title">
                            <h1>
                                <table>
                                    <tr>
                                        <td style="padding-right:10px;">
                                      <field name="name" required="1" placeholder="le nom" />
                                  </td>
                                        <td style="padding-right:10px;">
                                             <field name="prix" placeholder="le prix" />
                                         </td>
                                    </tr>
                                </table>
                            </h1>
                        </div>
                    </sheet>
                </form>
            </field>
    </record>
    <!-- end view_formation_form-->
    
    <!-- view_formation_tree-->
    <record id="view_formation_tree" model="ir.ui.view">
            <field name="name">formation.formation.tree</field>
            <field name="model">formation.formation</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <tree string="formations">
                    <field name="name" />
                    <field name="prix" />
                </tree>
            </field>
    </record>
    <!-- end of view_formation_tree-->    

    <!-- action_view_formation_list-->
    <record model="ir.actions.act_window" id="action_view_formation_list">
        <field name="name">liste des formations</field> 
        <field name="res_model">formation.formation</field> 
        <field name="view_type">form</field> 
        <field name="view_mode">tree,form</field> 
        <field name="domain">[]</field> 
        <field name="help" type="html"> 
            <p class="oe_view_nocontent_create">Crée une nouvelle formation. </p>
        </field>
    </record>
    <!-- end of action_view_formation_list-->


 



Interface Salle:
    <!-- view_salle_form-->
    <record id="view_salle_form" model="ir.ui.view">
            <field name="name">salle.salle.form</field>
            <field name="model">salle.salle</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <form string="salle">
                    <sheet>
                        <div class="oe_title">
                            <h1>
                                <table>
                                    <tr>
                                        <td style="padding-right:10px;"><field name="name" placeholder="le nom" /></td>
                                        <td style="padding-right:10px;"><field name="nb_place" placeholder="le nombre de place" /></td>
                                        <td style="padding-right:10px;"><field name="libre" placeholder="esque la est libre ??" /></td>
                                    </tr>
                                </table>
                            </h1>
                        </div>
                    </sheet>
                </form>
            </field>
    </record>
    <!-- end view_salle_form-->
    
    <!-- view_salle_tree-->
    <record id="view_salle_tree" model="ir.ui.view">
            <field name="name">salle.salle.tree</field>
            <field name="model">salle.salle</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <tree string="salles">
                    <field name="name" />
                    <field name="nb_place" />
                    <field name="libre" />
                </tree>
            </field>
    </record>
    <!-- end of view_salle_tree-->   

    <!-- action_view_salle_list-->
    <record model="ir.actions.act_window" id="action_view_salle_list">
        <field name="name">liste des salles</field> 
        <field name="res_model">salle.salle</field> 
        <field name="view_type">form</field> 
        <field name="view_mode">tree,form</field> 
        <field name="domain">[]</field> 
        <field name="help" type="html"> 
            <p class="oe_view_nocontent_create">ajouter un nouvelle salle. </p>
        </field>
    </record>
    <!-- end of action_view_salle_list-->

 

Interface Session:
    <!-- view_session_form-->
    <record id="view_session_form" model="ir.ui.view">
            <field name="name">session.session.form</field>
            <field name="model">session.session</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <form string="session">
                    <sheet>
                        <div class="oe_title">
                            <h1>
                                <table>
                                    <tr>
                                        <td style="padding-right:10px;"><field name="name" placeholder="le nom" /></td>
                                        <td style="padding-right:10px;"><field name="nb_participants" placeholder="le nombre de participants" /></td>
                                        <td style="padding-right:10px;"><field name="date_debut" placeholder="la date debut" /></td>
                                        <td style="padding-right:10px;"><field name="date_fin" placeholder="la date fin" /></td>
                                        <td style="padding-right:10px;"><field name="duree" placeholder="la duree de cette session" /></td>
                                    </tr>
                                </table>
                            </h1>
                        </div>
                    </sheet>
                </form>
            </field>
    </record>
    <!-- end view_session_form-->
    
    <!-- view_session_tree-->
    <record id="view_session_tree" model="ir.ui.view">
            <field name="name">session.session.tree</field>
            <field name="model">session.session</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <tree string="sessions">
                    <field name="name" />
                    <field name="nb_participants" />
                    <field name="date_debut" />
                    <field name="date_fin" />
                    <field name="duree" />
                </tree>
            </field>
    </record>
    <!-- end of view_session_tree-->   

    <!-- action_view_session_list-->
    <record model="ir.actions.act_window" id="action_view_session_list">
        <field name="name">liste des session</field> 
        <field name="res_model">session.session</field> 
        <field name="view_type">form</field> 
        <field name="view_mode">tree,form</field> 
        <field name="domain">[]</field> 
        <field name="help" type="html"> 
            <p class="oe_view_nocontent_create">ajouter un nouvelle session. </p>
        </field>
    </record>
    <!-- end of action_view_session_list-->

 

Interface Candidat:
    <!-- view_candidat_form-->
    <record id="view_candidat_form" model="ir.ui.view">
            <field name="name">candidat.candidat.form</field>
            <field name="model">candidat.candidat</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <form string="candidat">
                    <sheet>
                        <div class="oe_title">
                            <h1>
                                <table>
                                    <tr>
                                        <td style="padding-right:10px;"><field name="name" placeholder="le nom" /></td>
                                        <td style="padding-right:10px;"><field name="num_ins" placeholder="le numéro d'inscription" /></td>
                                    </tr>
                                </table>
                            </h1>
                        </div>
                    </sheet>
                </form>
            </field>
    </record>
    <!-- end view_candidat_form-->
    
    <!-- view_candidat_tree-->
    <record id="view_candidat_tree" model="ir.ui.view">
            <field name="name">candidat.candidat.tree</field>
            <field name="model">candidat.candidat</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <tree string="candidats">
                    <field name="name" />
                    <field name="num_ins" />
                </tree>
            </field>
    </record>
    <!-- end of view_candidat_tree-->   

    <!-- action_view_candidat_list-->
    <record model="ir.actions.act_window" id="action_view_candidat_list">
        <field name="name">liste des candidats</field> 
        <field name="res_model">candidat.candidat</field> 
        <field name="view_type">form</field> 
        <field name="view_mode">tree,form,kanban</field> 
        <field name="domain">[]</field> 
        <field name="help" type="html"> 
            <p class="oe_view_nocontent_create">ajouter un nouveau candidat. </p>
        </field>
    </record>
    <!-- end of action_view_candidat_list-->
    <!-- candidat_search_view-->
    <record model="ir.ui.view" id="candidat_search_view">
        <field name="name">candidat.search</field>
        <field name="model">candidat.candidat</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="num_ins"/>
            </search>
        </field>
    </record>
    <!-- end of candidat_search_view-->

    <!-- candidat_kanban-->
    <record id="candidat_kanban" model="ir.ui.view">
            <field name="name">candidat.kanban</field>
            <field name="model">candidat.candidat</field>
            <field name="arch" type="xml">
                <kanban>
                    <!--field name="sessionId"/-->
                    <templates>
                        <t t-name="kanban-box">
                            <div class="oe_resource_details">
                                <ul>
                                    <li>
                                        <field name="name"/>
                                    </li>
                                    <li>
                                        <field name="num_ins"/>
                                    </li>
                                </ul>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
    </record>
    <!-- end of candidat_kanban-->

 
Interface Formateur:
    <!-- view_formateur_form-->
    <record id="view_formateur_form" model="ir.ui.view">
            <field name="name">formateur.formateur.form</field>
            <field name="model">formateur.formateur</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <form string="formateur">
                    <sheet>
                        <div class="oe_title">
                            <h1>
                                <table>
                                    <tr>
                                        <td style="padding-right:10px;"><field name="matricule" required="1" placeholder="entrer matricule" /></td>
                                        <td style="padding-right:10px;"><field name="name" placeholder="le nom" /></td>
                                        <td style="padding-right:10px;"><field name="diplome" placeholder="le diplome" /></td>
                                    </tr>
                                </table>
                            </h1>
                        </div>
                    </sheet>
                </form>
            </field>
    </record>
    <!-- end view_formateur_form-->
    
    <!-- view_formateur_tree-->
    <record id="view_formateur_tree" model="ir.ui.view">
            <field name="name">formateur.formateur.tree</field>
            <field name="model">formateur.formateur</field>
            <field name="priority" eval="8" />
            <field name="arch" type="xml">
                <tree string="formateurs">
                    <field name="matricule" />
                    <field name="name" />
                    <field name="diplome" />
                </tree>
            </field>
    </record>
    <!-- end of view_formateur_tree-->   

    <!-- action_view_formateur_list-->
    <record model="ir.actions.act_window" id="action_view_formateur_list">
        <field name="name">liste des formateurs</field> 
        <field name="res_model">formateur.formateur</field> 
        <field name="view_type">form</field> 
        <field name="view_mode">tree,form,kanban</field> 
        <field name="domain">[]</field> 
        <field name="help" type="html"> 
            <p class="oe_view_nocontent_create">ajouter un nouveau formateur. </p>
        </field>
    </record>
    <!-- end of action_view_formateur_list-->

    <!-- formateur_search_view-->
    <record model="ir.ui.view" id="formateur_search_view">
        <field name="name">formateur.search</field>
        <field name="model">formateur.formateur</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <field name="matricule"/>
                <field name="diplome"/>
            </search>
        </field>
    </record>
    <!-- end of formateur_search_view-->

    <!-- formateur_kanban-->
    <record id="formateur_kanban" model="ir.ui.view">
            <field name="name">formateur.kanban</field>
            <field name="model">formateur.formateur</field>
            <field name="arch" type="xml">
                <kanban>
                    <!--field name="sessionId"/-->
                    <templates>
                        <t t-name="kanban-box">
                            <div class="oe_resource_details">
                                <ul>
                                    <li>
                                        <field name="name"/>
                                    </li>
                                    <li>
                                        <field name="matricule"/>
                                    </li>
                                    <li>
                                        <field name="diplome"/>
                                    </li>
                                </ul>
                            </div>
                        </t>
                    </templates>
                </kanban>
            </field>
    </record>
    <!-- end of formateur_kanban-->



Interface menu:
    <!-- menu items-->
    <menuitem id="header_menu" name="gestion formation"/>
        <menuitem id="menu_gestion_formation" name="gestion formation" parent='header_menu'/>
            <menuitem id="menu_formation" name="formation" parent="menu_gestion_formation" 
            action="action_view_formation_list"/>

            <menuitem id="menu_formateur" name="formateur" parent="menu_gestion_formation" 
            action="action_view_formateur_list"/>

            <menuitem id="menu_candidat" name="candidat" parent="menu_gestion_formation" 
            action="action_view_candidat_list"/>

            <menuitem id="menu_salle" name="salle" parent="menu_gestion_formation" 
            action="action_view_salle_list"/>   
                  
            <menuitem id="menu_session" name="session" parent="menu_gestion_formation" 
            action="action_view_session_list"/>      
    <!-- end of menu items-->

 


4. Lié les objets entre eux en utilisant les champs relationnelles (selon le diagramme).

class Candidat(models.Model):
	…..
    session = fields.Many2many('session')

class Formateur(models.Model):
	…..
    session = fields.Many2many('session')

class Formation(models.Model):
	…..
    sessionId = fields.One2many('session' , 'formationId' , "refernece des session")

class Salle(models.Model):
	…...
    session = fields.Many2many('session')

class Session(models.Model):
	…..
    formationId = fields.Many2one('formation.formation', ondelete="cascade")
    categorie = fields.Char(string='categorie',compute='_onchange_formation')
    salle_ids = fields.Many2many('formation.salle', 'session_salle', 'session_id', 'salle_id')
    candidat_ids = fields.Many2many('formation.candidat', 'session_candidat', 'session_id', 'candidat_id')
    formateur_ids = fields.Many2many('formation.formateur', 'session_formateur', 'session_id', 'formateur_id')


Et on ajoute ces lignes au tree de session :
                    <field name="salle_ids"/>
                    <field name="formateur_ids"/>
                    <field name="candidat_ids"/>

Partie 2 :
1. Implémenter les besoins suivants :
 	• La durée de la session est calculable selon la date de début et la date de fin.
    @api.one
    @api.depends('date_debut', 'date_fin')
    def compute_duree(self):
        if self.date_debut and self.date_fin:
            date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
            date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
            self.duree = date_fin - date_debut
        else:
            self.duree = False

 	• La date de début ne doit pas être supérieure à la date de fin.
    @api.one
    @api.constrains('date_debut', 'date_fin')
    def verif(self):
        date_debut = datetime.strptime(self.date_debut, "%Y-%m-%d")
        date_fin = datetime.strptime(self.date_fin, "%Y-%m-%d")
        if date_debut > date_fin:
            raise ValidationError("erreur date fin superieur")

• La capacité des salles est 20 places par défaut (possible de la modifier par la suite)
     nb_place = fields.Integer(default=20)

 	• Quand la formation de la session change, la catégorie de la formation est récupérée.
    @api.one
    @api.depends('formationId')
    def _onchange_formation(self):
        self.categorie = self.formationId.categorie

 	• Le numéro d’inscription du candidat est unique. Pareil pour le matricule du formateur.
    _sql_constraints = [
        ('num_ins_unique', 'unique(num_ins)', 'numero d\' inscription existe  deja!')
    ]

    _sql_constraints = [
        ('matricule_unique', 'unique(matricule)', 'matricule existe  deja!')
    ]
5. Gérer les droit d’accès de l’application « Centre Formation » en sachant que :
 	• Il y a 2 profiles d’utilisateur : Gérant & Secrétaire.
 	• Le Gérant a tous les droits et pour tous les objets.
 	• La Secrétaire peut :
 		 Consulter tous les objets.
 		 Créer, modifier, et supprimer des candidats et des formateurs.
 		 Modifier les salles.
• Le bouton « Crée les attestations » est accessible que par le gérant.
Il faut cree le fichier xml suivant :
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <data>
        <record id="groupe_secretaire" model="res.groups">
            <field name="name">Secretaire</field>
        </record>

        <record id="groupe_gerant" model="res.groups">
            <field name="name">Gerant</field>
        </record>

    </data>
</odoo>

Et on donne les droits pour les utilisateurs dans le fichier ir.model.access.csv :

    id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
    
    access_candidat_sec,candidat_secretaire,model_formation_candidat,groupe_secretaire,1,1,1,1
    access_candidat_ger,candidat_gerant,model_formation_candidat,groupe_gerant,1,1,1,1
    
    access_session_sec,session_secretaire,model_session,groupe_secretaire,1,0,0,0
    access_session_ger,session_gerant,model_session,groupe_gerant,1,1,1,1
    
    access_attestation_sec,attestation_secretaire,model_formation_attestation,groupe_secretaire,1,0,0,0
    access_attestation_ger,attestation_gerant,model_formation_attestation,groupe_gerant,1,1,1,1
    
    access_formateur_sec,formateur_secretaire,model_formation_formateur,groupe_secretaire,1,1,1,1
    access_formateur_ger,formateur_gerant,model_formation_formateur,groupe_gerant,1,1,1,1
    
    access_salle_sec,salle_secretaire,model_formation_salle,groupe_secretaire,1,1,1,1
    access_salle_ger,salle_gerant,model_formation_salle,groupe_gerant,1,1,1,1
    
    access_formation_sec,formation_secretaire,model_formation_formation,groupe_secretaire,1,1,1,1
    access_formation_ger,formation_gerant,model_formation_formation,groupe_gerant,1,0,0,0



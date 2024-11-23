"""
Think... Docstring cbe_data
"""
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

filepath = os.getenv('FILEPATH')

dtype_dict = {
    'EntityNumber': str,
    'Language': str,
    'TypeOfDenomination': str,
    'Denomination':str,
    'ActivityGroup': str,
    'NaceVersion': str,
    'NaceCode': str,
    'Classification':str,
    'EstablishmentNumber': str,
    'StartDate': str,
    'EnterpriseNumber': str,
    'TypeOfAddress': str,
    'CountryNL': str,
    'CountryFR': str,
    'Zipcode': str,
    'MunicipalityNL': str,
    'MunicipalityFR': str,
    'StreetNL': str,
    'StreetFR': str,
    'HouseNumber': str,
    'Box': str,
    'ExtraAddressInfo': str,
    'DateStrikingOff': str,
    'Status': str,
    'JuridicalSituation': str,
    'TypeOfEnterprise': str,
    'JuridicalForm': str,
    'JuridicalFormCAC': str,
}

activity = pd.read_csv('data/activity.csv', dtype=dtype_dict)
address = pd.read_csv('data/address.csv', dtype=dtype_dict)
denomination = pd.read_csv('data/denomination.csv', dtype=dtype_dict)
enterprise = pd.read_csv('data/enterprise.csv', dtype=dtype_dict)
establishment = pd.read_csv('data/establishment.csv', dtype=dtype_dict)


StopReason_dct = {
    '006': 'Cessation due to company number replacement', 
    '010': 'Ex officio dissolution', 
    '011': 'Cessation of activities in Belgium (foreign entity)', 
    '012': 'Voluntary dissolution - liquidation', 
    '013': 'Judicial dissolution or nullity', 
    '014': 'Closure of liquidation', 
    '015': 'Cessation of an entity without legal personality', 
    '016': 'Cessation of activity entity - natural person', 
    '017': 'Transfer of a registered entity - natural person', 
    '018': 'Cessation during identification', 
    '019': 'Cessation of an EDRL or non-EU entity', 
    '021': 'Merger by acquisition', 
    '022': 'Merger by formation of a new entity', 
    '023': 'Division', 
    '024': 'Division by acquisition', 
    '025': 'Division by formation of new entities', 
    '026': 'Mixed division', 
    '050': 'Cessation during opening of bankruptcy procedure', 
    '051': 'Closing of bankruptcy procedure with excusability', 
    '052': 'Closing of bankruptcy procedure with inexcusability', 
    '053': 'Closing of bankruptcy procedure', 
    '054': 'Cessation during closure of bankruptcy procedure', 
    '080': 'Cessation of an establishment unit', 
    '081': 'Transfer of an establishment unit', 
    '082': 'Transfer of an entity', 
    '090': 'Legal abolition', 
    '100': 'Ex-officio striking off', 
    '111': 'Striking off following the cessation in a register in the EEA', 
    '120': 'Termination of a branch', 
    '999': 'Cancelled file'
    }

TypeOfEnterprise_dct = {                    # Not yet certain
    '1': 'Registered entity natural person', 
    '2': 'Registered entity legal person'
    }

Status_dct = {
    'AC': 'Active', 
    'AF': 'Closed', 
    'AN': 'Cancelled', 
    'BK': 'Identified', 
    'JU': 'Legal creation', 
    'ST': 'Stopped'
    }

JuridicalSituation_dct = {
    '000': 'Normal situation', 
    '001': 'Legal incorporation', 
    '002': 'Extension', 
    '003': 'Company number replacement', 
    '006': 'Cessation due to company number replacement', 
    '010': 'Ex officio dissolution', 
    '011': 'Cessation of activities in Belgium (foreign entity)', 
    '012': 'Voluntary dissolution - liquidation', 
    '013': 'Judicial dissolution or nullity', 
    '014': 'Closure of liquidation', 
    '015': 'Cessation of an entity without legal personality', 
    '016': 'Cessation of activity entity - natural person', 
    '017': 'Transfer of a registered entity - natural person', 
    '018': 'Cessation during identification', 
    '019': 'Cessation of an EDRL or non-EU entity', 
    '020': 'Shares held by a single shareholder', 
    '021': 'Merger by acquisition',
    '022': 'Merger by formation of a new entity', 
    '023': 'Division', 
    '024': 'Division by acquisition', 
    '025': 'Division by formation of new entities', 
    '026': 'Mixed division', 
    '030': 'Judicial settlement before bankruptcy', 
    '031': 'Judicial settlement after bankruptcy', 
    '040': 'Provisional deferment of payment', 
    '041': 'Permanent deferment of payment', 
    '042': 'Deferment of payment revocation', 
    '043': 'End of deferment', 
    '048': 'Opening of bankruptcy procedure with excusability', 
    '049': 'Opening of bankruptcy procedure with inexcusability', 
    '050': 'Opening of bankruptcy procedure', 
    '051': 'Closing of bankruptcy procedure with excusability', 
    '052': 'Closing of bankruptcy procedure with inexcusability', 
    '053': 'Closing of bankruptcy procedure', 
    '090': 'New statutes', 
    '091': 'Deferment (judicial reorganisation)', 
    '100': 'Entity identification', 
    '111': 'Striking off following the cessation in register in the EEA', 
    '112': 'Reopening liquidation', 
    '999': 'Cancelled file'
    }

Event_dct = {
    '01': 'Revoked bankruptcy', 
    '02': 'Rehabilitation', 
    '03': 'Discharge', 
    '04': 'Partial debt write-off', 
    '05': 'Debt write-off', 
    '06': 'Debt write-off refusal', 
    '07': 'Revocation of the dissolution'
    }

JuridicalForm_dct = {
    '001': 'European cooperative society', 
    '002': 'Pension scheme organisation', 
    '003': 'VAT-group', 
    '006': 'Cooperative society with unlimited liability', 
    '007': 'Cooperative society with unlimited liability (profit share)', 
    '008': 'Cooperative society with limited liability', 
    '009': 'Cooperative society with limited liability (profit share)', 
    '010': 'Private limited liability company', 
    '011': 'General partnership', 
    '012': 'Ordinary limited partnership', 
    '013': 'Partnership limited by shares', 
    '014': 'Public limited company', 
    '015': 'Private limited liability company', 
    '016': 'Cooperative society (old regime)', 
    '017': 'Non-profit organisation', 
    '018': 'Public utility institution', 
    '019': 'Health fund / Mutual health insurance / National union of health '
    'funds', 
    '020': 'Professional union', 
    '021': 'Private mutual insurance fund', 
    '022': 'International scientific organisation under Belgian law', 
    '023': 'Private foreign association with establishment in Belgium', 
    '025': 'Agricultural company', 
    '026': 'Private foundation', 
    '027': 'European company (Societas Europaea)', 
    '028': 'Non-profit institution', 
    '029': 'Public utility foundation', 
    '030': 'Foreign entity', 
    '040': 'Congolese company', 
    '051': 'Other private organisation with legal personality', 
    '060': 'Economic interest grouping with registered seat in Belgium', 
    '065': 'European economic assoc with registered seat in Belgium', 
    '070': 'Co-ownership association', 
    '106': 'Cooperative society with unlimited liability governed by public law', 
    '107': 'Cooperative society with unlimited liability governed by public law'
    ' (profit share)', 
    '108': 'Cooperative society with limited liability governed by public law', 
    '109': 'Cooperative society with limited liability governed by public law'
    ' (profit share)', 
    '110': 'State, Province, Region, Community', 
    '114': 'Public limited company', 
    '116': 'Cooperative society governed by public law (old regime)', 
    '117': 'Public non-profit association', 
    '121': 'Public mutual insurance fund', 
    '123': 'Professional corporations - Orders', 
    '124': 'Public institution', 
    '125': 'International non-profit association', 
    '127': 'Pawnshop', 
    '128': 'Cult', 
    '129': 'Polders and water boards', 
    '151': 'Other legal form', 
    '160': 'Foreign or international public organisations', 
    '200': 'Company in formation', 
    '206': 'Civil society as an unlimited liability and united CS', 
    '208': 'Civil society in the form of a limited liability CS', 
    '211': 'Civil society in the form of a collective society', 
    '212': 'Civil society in the form of a limited partnership', 
    '213': 'Civil society in the form of a limit partnership with shares', 
    '214': 'Civil society in the form of a public limited company', 
    '215': 'Civil society in the form of a private limited liability company', 
    '217': 'European political party ', 
    '218': 'European political foundation', 
    '225': 'Civil society in the form of an agricultural company', 
    '230': 'Foreign entity with property in Belgium (with legal personality)', 
    '235': 'Foreign entity without Belgian establishment unit with VAT '
    'representation', 
    '260': 'Econ. assoc wo regist. seat but with est. unit in Belgium', 
    '265': 'Europ. Econ. assoc wo reg.seat but with est. unit in Belgium', 
    '301': 'Federal public service', 
    '302': 'Federal public planning service', 
    '303': 'Other federal services', 
    '310': 'Flemish region and Flemish community authorities', 
    '320': 'Walloon region authorities', 
    '325': 'International non-profit association governed by public law', 
    '330': 'Brussels-Capital region authorities', 
    '340': 'French community authorities', 
    '350': 'German-speaking community authorities', 
    '370': 'Ministry of Economic Affairs', 
    '371': 'Ministry of Foreign Affairs', 
    '372': 'Ministry of Agriculture', 
    '373': 'Ministry for Middle Class', 
    '374': 'Ministry of Road Works', 
    '375': 'Ministry of National Defence', 
    '376': 'Ministry of National Education and Culture', 
    '377': 'Ministry of Employment and Labour', 
    '378': 'Ministry of Finance', 
    '379': 'Ministry of Home Affairs', 
    '380': 'Ministry of Justice', 
    '381': 'Ministry of Social Welfare', 
    '382': 'Ministry of Public Health and Family', 
    '383': 'The services of the Prime Minister', 
    '384': 'Ministry of Traffic and Infrastructure', 
    '385': 'Ministry of the Flemish Community', 
    '386': 'Ministry of the French Community', 
    '387': 'Ministry of the Brussels-Capital Region', 
    '388': 'Ministry of the Walloon Region', 
    '389': 'Ministry of the German-speaking Community', 
    '390': 'Ministry of Public Service', 
    '391': 'Ministry of Self-Employed and Agriculture', 
    '392': 'Ministry of Social Affairs, Public Health and Environment', 
    '393': 'Miscellaneous', 
    '400': 'Provincial authorities', 
    '401': 'Organisations registered through the ONSSAPL', 
    '411': 'Cities and municipalities', 
    '412': 'Pubic social action centre', 
    '413': 'Local police', 
    '414': 'Intercommunal', 
    '415': 'Project association', 
    '416': 'Service provider association (Flemish region)', 
    '417': 'Representative association (Flemish region)', 
    '418': 'Autonomous municipal company', 
    '419': 'Autonomous provincial company', 
    '420': 'CPAS / OCMW Association', 
    '421': 'Prezone', 
    '422': 'Hulpverleningszone', 
    '451': 'Organisations registered with the O.N.P', 
    '452': 'Organis. regist. with the public admin. Pensions (Finance)', 
    '453': 'Foreign listed company without Belgian establishment unit', 
    '454': 'Foreign ent. with property in Belgium (without legal pers.)', 
    '506': 'Cooperative society with unlimited liability and a social '
    'objective', 
    '508': 'Cooperative society with limited liability and a social objective', 
    '510': 'Unipersonal private limited liability company with a social '
    'objective', 
    '511': 'General partnership with a social objective', 
    '512': 'Ordinary limited partnership with a social objective', 
    '513': 'Partnership limited by shares with a social objective', 
    '514': 'Public limited company with a social objective', 
    '515': 'Private limited liability company with a social objective', 
    '560': 'Economic interest grouping with a social objective', 
    '606': 'Cooperative society with unlimited liability and a social objective', 
    '608': 'Cooperative society with limited liability and a social objective', 
    '610': 'Private limited company', 
    '612': 'Limited partnership', 
    '614': 'Public limited company with a social objective', 
    '616': 'Private limited company governed by public law', 
    '617': 'Limited partnership governed by public Law', 
    '651': 'Other institution with a social objective (public)', 
    '701': 'Unlawful commercial company', 
    '702': 'Common law company', 
    '703': 'Temporary company', 
    '704': 'Internal company', 
    '706': 'Cooperative society', 
    '716': 'Cooperative society governed by public law', 
    '721': 'Company or association without legal personality', 
    '722': 'Temporary association', 
    '723': 'Expense association', 
    '724': 'Trade union', 
    '790': 'Miscellaneous without legal personality', 
    '999': 'Unkown legal form (NSSO)'
    }

Function_dct = {
    '00001': 'Founder registered entity natural person', 
    '00002': 'General agent', 
    '00003': 'Associate or member', 
    '00004': 'VAT-grouping representative', 
    '00005': 'Deputy permanent representative', 
    '10001': 'Founder of a body without legal personality', 
    '10002': 'Director', 
    '10003': 'Permanent representative', 
    '10004': 'Person in charge of daily management', 
    '10005': 'Member of the management committee', 
    '10006': 'Manager', 
    '10007': 'Managing Director', 
    '10008': 'Property manager', 
    '10010': 'Chairman', 
    '10011': 'Secretary', 
    '10012': 'Treasurer', 
    '10013': 'Managing Director', 
    '10014': 'Deputy Managing Director', 
    '10015': 'Vice President', 
    '10016': 'Member of the supervisory board', 
    '10017': 'Member of the management committee', 
    '10018': 'Legal person representative', 
    '10020': 'Statutory Auditor', 
    '10021': 'Permanent representative of the auditor', 
    '10022': 'Representative (non-administrator)', 
    '10023': 'General administrator', 
    '10030': 'Administrator', 
    '10031': 'Legal representative', 
    '10032': 'Representative (branch)', 
    '10033': 'Secretary (Flemish Region)', 
    '10041': 'Mayor', 
    '10042': 'Secretary / Managing director', 
    '10045': 'Member of area association', 
    '10500': 'EDRL contact person', 
    '11000': 'Supply solicitor', 
    '12000': 'Acting bailiff', 
    '90000': 'Receiver (designated by court)', 
    '90001': 'Curator (designated by court)', 
    '90002': 'Deferment auditor (designated by court)', 
    '90003': 'Deferment auditor (designated by court)', 
    '90004': 'Judicial board (prodigals)', 
    '90005': 'Judicial trustee'
    }

StopReasonFunction_dct = {
    '002': 'Deceased before start exercise', 
    '003': 'Decease', 
    '004': 'Dismissal', 
    '005': 'End of assignment', 
    '006': 'Cessation due to company number replacement', 
    '010': 'Ex officio dissolution', 
    '011': 'Cessation of activities in Belgium (foreign entity)', 
    '012': 'Voluntary dissolution - liquidation', 
    '013': 'Judicial dissolution or nullity', 
    '014': 'Closure of liquidation', 
    '015': 'Cessation of an entity without legal personality', 
    '016': 'Cessation of activity entity - natural person', 
    '017': 'Transfer of a registered entity - natural person', 
    '018': 'Cessation during identification', 
    '019': 'Cessation of an EDRL or non-EU entity', 
    '021': 'Merger by acquisition', 
    '022': 'Merger by formation of a new entity', 
    '023': 'Division', 
    '024': 'Division by acquisition', 
    '025': 'Division by formation of new entities', 
    '026': 'Mixed division', 
    '030': 'Prohibition of profession', 
    '035': 'Cessation of exemption', 
    '050': 'Cessation during bankruptcy procedure', 
    '051': 'Closure of bankruptcy procedure with excusability', 
    '052': 'Closure of bankruptcy procedure with inexcusability', 
    '053': 'Closure of bankruptcy procedure', 
    '054': 'Cessation during closure of bankruptcy procedure', 
    '080': 'Cessation of an establishment unit', 
    '081': 'Transfer of an establishment unit', 
    '082': 'Transfer of an entity', 
    '100': 'Ex-officio striking off', 
    '111': 'Striking off following the cessation in a register in the EEA', 
    '200': 'Card not exchanged RD of 11 March 2013', 
    '998': 'Discontinuation ', 
    '999': 'File cancelled'
    }

Profession_dct = {
    '00006': 'Fairground operator',
    '20001': 'Joiner - carpenter contractor',
    '20002': 'Central heating installer',
    '20003': 'Plasterer - cement contractor',
    '20005': 'Insurance broker',
    '20006': 'Hairdresser',
    '20007': 'Miller',
    '20008': 'Painting contractor',
    '20009': 'Indigenous cereals trader',
    '20010': 'Wholesale meat trader',
    '20011': 'Optician',
    '20012': 'Bicycle mechanic',
    '20013': 'Moped mechanic',
    '20014': 'Scooter mechanic',
    '20015': 'Masonry and concrete works contractor',
    '20016': 'Stone carving contractor',
    '20017': 'Photographer',
    '20018': 'Solid fuel dealer - retailer',
    '20019': 'Marble works contractor',
    '20020': 'Fodder and straw dealer',
    '20021': 'Tiling contractor',
    '20022': 'Electrician installation',
    '20023': 'Upholsterer - floor and wall covering contractor',
    '20024': 'Watchmaker - clock repairs',
    '20025': 'Dental technician',
    '20026': 'Garage mechanic - repair services',
    '20027': 'Glazing contractor',
    '20028': 'Liquid fuel dealer - retailer',
    '20029': 'Second-hand car dealer ',
    '20030': 'Sanitary facilities installer and plumbing',
    '20031': 'Individual gas heating appliance installer',
    '20032': 'Contractor zinc works and metal roofs',
    '20033': 'Contractor construction non-metal roofs',
    '20034': 'Refrigeration contractor',
    '20035': 'Dry cleaning - dyeing services',
    '20036': 'Laundry services',
    '20037': 'Coachbuilder - body repairer',
    '20038': 'Funeral director',
    '20039': 'Manufacturer - installer neon signs',
    '20040': 'Restaurateur or catering service-banquet organiser',
    '20041': 'Contractor weatherproofing of structures',
    '20042': 'Demolition works contractor',
    '20043': 'Baker - confectioner',
    '20044': 'Beautician',
    '20045': 'Butcher - specialist butcher',
    '20046': 'Mobile trade',
    '20047': 'Meat product retailer',
    '20048': "Itinerant activity at the consumer's home (Brussels Cap. R.)",
    '20050': 'Timeshare sales',
    '20090': 'Knowledge of basic management',
    '20091': 'Retailer',
    '20099': 'Non SME dispensation',
    '20100': 'Motorised  vehicles - inter-sectoral professional competence',
    '20101': 'Bicycles',
    '20102': 'Vehicles up to 3.5 tonnes',
    '20103': 'Vehicles over 3.5 tonnes',
    '20201': 'Structural works',
    '20202': 'Ceiling installation, cement works, screeds',
    '20203': 'Tiling, marble, natural stone',
    '20204': 'Roofs, weatherproofing',
    '20205': 'Joinery (installation/repair) and glazing',
    '20206': 'General carpentry',
    '20207': 'Finishing works (paint and wallpaper)',
    '20208': 'Installation (heating, air conditioning, sanitary, gas)',
    '20209': 'Electrotechnical services',
    '20210': 'General contractor',
    '20301': 'Hairdresser',
    '20302': 'Beautician',
    '20303': 'Pedicure',
    '20304': 'Masseur/masseuse',
    '20305': 'Optician',
    '20306': 'Dental technician',
    '20307': 'Funeral director ',
    }

Exempted_dct = {
    '001': 'Acquired rights : act at time of entry in force of regulat',
    '002': 'Company is no SME (art. 2, SME-pl 10/2/98)',
    '003': 'Real estate agent dispensation (art. 4, SME-pl 10/2/98)',
    '004': 'Real estate agent-trainee dispensation (art. 4, SME-pl 10/2/98)',
    '005': 'Insurance agent dispensation (art. 4, SME-pl 10/2/98)',
    '006': 'Insurance broker dispensation (art. 4, SME-pl 10/2/98)',
    '007': 'Driving school dispensation (art. 4, SME-pl 10/2/98)',
    '008': 'Passenger transport dispensation (art. 4, SME-pl 10/2/98)',
    '009': 'Road haulage dispensation  (art. 4, SME-pl 10/2/98)',
    '010': 'Transport by waterway dispensation  (art. 4, SME-pl 10/2/98)',
    '011': 'Home sales dispensation (art. 4, SME-pl 10/2/98)',
    '012': 'Surviving partner (art. 10, SME-pl 10/2/98)',
    '013': 'Child of deceased  manager (art. 11,  SME-pl 10/2/98)',
    '014': 'Transferee of a enterprise (art. 11, SME-pl 10/2/98)',
    '015': 'No decision of establishment council (art. 3§5, act 26/6/02)',
    '016': 'Banking and investment serv dispensation (art. 4,  SME-pl 10/2/98)',
    '017': 'Directive 2005/36 professional qualifications dispensation',
    }

LinkedEnterprise_dct = {
    '001': 'Creates an establishment unit ',
    '002': 'Is divided in',
    '003': 'Is absorbed by',
    '004': 'Is replaced by (only for doubles)',
    '005': 'Is transferred to',
    '006': 'Unknown relationship',
    '007': 'Creates branch',
    }

StopReasonLinkedEnterprise_dct = {
    '006': 'Cessation due to replacement double entity',
    '010': 'Dissolution due to expiration of term',
    '011': 'Cessation of activities',
    '012': 'Early dissolution',
    '013': 'Legal dissolution',
    '014': 'Closure of the liquidation',
    '015': 'Cessation (company without legal personality)',
    '016': 'Cessation of activity natural person',
    '017': 'Transfer of a registered entity natural person',
    '018': 'Cessation during identification',
    '019': 'Cessation of an EDRL or non EU entity',
    '021': 'Merger by acquisition',
    '022': 'Merger by formation of a new company',
    '023': 'Division',
    '024': 'Division by absorption',
    '025': 'Division by formation of new companies',
    '026': 'Mixed division',
    '050': 'Cessation during bankruptcy procedure',
    '051': 'Closure of bankruptcy procedure with excusability',
    '052': 'Closure of bankruptcy procedure without excusability',
    '053': 'Judgement closure of bankruptcy procedure',
    '054': 'Cessation during closure of bankruptcy procedure',
    '080': 'Cessation of an establishment unit',
    '081': 'Transfer of an establishment unit',
    '082': 'Transfer of an entity',
    '090': 'New articles of association',
    '100': 'Ex-officio striking off',
    '111': 'Striking off following the cessation in a register in the EEA',
    '999': 'File cancelled',
    }

ActivityGroup_dct = {
    '001': 'BTW-activiteiten',
    '002': 'EDRL-activiteiten (Buitenlandse bedrijven zonder vestiging in '
    'België)',
    '003': 'Activiteiten',
    '004': 'Activiteiten federaal openbaar ambt',
    '005': 'RSZPPO-activiteiten (RSZ v. Prov. en Plaatselijke Overheden)',
    '006': 'RSZ-activiteiten',
    '007': 'Activiteiten gesubsidieerd onderwijs',
    }

Language_dct = {
    '1': 'French',
    '2': 'Dutch',
    '3': 'German',
    '4': 'English',
    }

TypeOfDenomination_dct = {
    '001': 'Name',
    '002': 'Abbreviation',
    '003': 'Trade Name',
    '004': 'Branch Name',
}
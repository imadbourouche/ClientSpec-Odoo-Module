# -*- coding: utf-8 -*-
{
	'name': "Client Spec",

	'summary': """Gestion Clients Grossiste""",

	'description': """
	Gestion client grossiste module pour :
	- Gerer client et commandes
	- Gerer assurances
	""",

	'depends': [
		'base',
		'sale_management'
	],

	'data': [
		'security/security.xml',
		'security/ir.model.access.csv',
		'views/clientspec.xml',
	],

	'demo': [
		'demo.xml',
	],
}
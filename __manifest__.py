{
    'name': 'helpdesk_ticket',
    'version': '1.0',
    'category': 'productivity',
    'summary': 'helpdesk_ticket',
    'description': """
    Modul HelpDesk
    """,
    'author': 'Amelia Tri Prismatiwi',
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/helpdesk_action.xml',
        'views/pivot.xml',
        'views/dashboard.xml',
        'views/template.xml',
        'report/ticket_detail.xml',
        'report/report.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',

    'qweb': [
        'static/xml*.xml',
    ]
}
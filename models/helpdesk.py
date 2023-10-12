from odoo import api, models, fields, _

class HelpdeskTicket(models.Model):
    _name = "helpdesk.ticket"
    _inherit = ["mail.thread"]
    _description = "Helpdesk Ticket"

    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))
    departemen = fields.Char(string='Departemen', required=True, tracking=True)
    divisi = fields.Char(string='Divisi', required=True, tracking=True)
    tanggal = fields.Date(string='Tanggal', default=fields.Date.today(), tracking=True)
    image = fields.Image(string='Image')
    state = fields.Selection([ 
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    helpdesk_ticket_ids = fields.One2many('helpdesk.ticket.line', 'helpdesk_ticket_id', string="Problems")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'
    
    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'


    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('helpdesk.ticket') or _('New')
        res = super(HelpdeskTicket, self).create(vals)
        return res

class HelpdeskTicketLine(models.Model): 
    _name = "helpdesk.ticket.line"
    _description = "Helpdesk Ticket Line"  

    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Ticket Id") 
    device_id = fields.Char(string='Device Id')
    problem_category = fields.Char(string='Problem Category')
    utility = fields.Char(string='Utility')
    note = fields.Text(string='Note')
    documents = fields.Binary(string='Documents')
    documents_name = fields.Char(string='Documents Name')
    


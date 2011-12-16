# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
error_page=URL(r=request,f='error')
if not session.recent1_companies: session.recent_companies=[]
if not session.pc_version: session.pc_version=[]



#def index():
 
    #return dict(table=plugin_jqgrid(db.laptops,columns=['id','Serial','Student','School'],col_widths={'id':50,'Serial':200,'Student':150,'School':100},width=600))
# Función que muestra la lista completa en modo invitado    
#def index():
    #class Virtual(object):
        #@virtualsettings(label=T('Information:'))
        #def virtualtooltip(self):
            #return T('This is a virtual tooltip for record %s' % self.laptops.id)
           
    #mytable = plugins.powerTable
    #mytable.datasource = db.laptops
    #mytable.virtualfields = Virtual()
    #mytable.headers = 'fieldname:capitalize'
    #mytable.dtfeatures['bJQueryUI'] = True
    #mytable.uitheme = 'smoothness'
    #mytable.extrajs = dict(tooltip={'value':'vitualtooltip'})
    #mytable.dtfeatures['sPaginationType'] = 'scrolling'
    #mytable.columns = ['laptops.id','laptops.Serial','laptops.User','laptops.Time','laptops.Info','laptops.Os']
    
    #return dict(table=mytable.create())

#@auth.requires_login()
def index():
    import main
    import urllib
    params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    mensaje = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params).read()
    count = db.sell_parts.id.count()
#    muvar = main.guitar()
#   test = muvar.printdetails()
#    mensaje = main.dimehola()    
    return dict(laptops=count, mensaje=mensaje)
    
#@auth.requires_login()
def edit_laptop():
    laptops_id=request.args(0)
    laptops=db.laptops[laptops_id]
    return dict(form=crud.update(db.laptops,laptops_id),laptops=laptops)
    
# muestra la lista completa en modo administrador   
#@auth.requires_login()
def view_laptops():
    laptops_id=request.args(0)
    laptops=db.laptops[laptops_id]
    return dict(laptops=laptops)
    
# "Tools" configuration    

#@auth.requires_login()  
def view_tools():
    
    tools=db(db.tools.id>0).select(orderby=db.tools.id)
   
    return dict(tools=tools)
    
def view2_tools():
    tools_id=request.args(0)
    tools=db.tools[tools_id]
    return dict(tools=tools)
    
def edit_tools():
    tools_id=request.args(0)
    tools=db.tools[tools_id]
    return dict (form=crud.update(db.tools,tools_id), tools=tools)
    
def add_tools():
    form=crud.create(db.tools)
    return dict (form=form)
    
    
            
            
# "laptops" configuration   
        
def edit_laptop():
    laptops_id=request.args(0)
    laptops=db.laptops[laptops_id]
    return dict(form=crud.update(db.laptops,laptops_id),laptops=laptops)            

def add_laptops():
    
    
    form=SQLFORM(db.laptops)
    if form.accepts(request.vars):response.flash="New  laptop #%i inserted" % form.vars.id
    return dict (form=form)
    
    
# "docs" Configuration
#@auth.requires_login()
def list_docs():
    docs=db(db.docs.id>0).select(orderby=db.docs.id)
    return dict(docs=docs)
    
@auth.requires_login()    
def add_docs():
    form=crud.create(db.docs)
    return dict(form=form)
    
@auth.requires_login()        
def edit_docs():
    docs_id=request.args(0)
    docs=db.docs[docs_id]
    return dict(form=crud.update(db.docs,docs_id),docs=docs)
        
#@auth.requires_login() 
def list_laptop():
    
 
    laptops=db(db.laptops.id>0).select(orderby=db.laptops.id)    
        
    form = plugin_appreport.REPORTFORM(table=db.laptops)
    if form.accepts(request.vars, session):
        laptops = db(form.prep_filter(filter = dict(form.vars))).select()
        html = response.render('default/gen_report.html',  dict(laptops = laptops))
        css = response.render('default/web20.css', dict (laptops = laptops))
        return plugin_appreport.REPORTPISA (html=html, title="my report")    
    
    return dict(laptops=laptops, form=form)
    
    
# "Movements" configuration    

@auth.requires_login()
def list_movs():
    movements=db(db.movements.id>0).select(orderby=db.movements.id)
    
    form = plugin_appreport.REPORTFORM(table=db.movements)    
    if form.accepts(request.vars, session):
        movements = db(form.prep_filter(filter = dict(form.vars))).select()
        html = response.render('default/gen_report_movs.html', dict(movements = movements))
        css = response.render('default/web20.css', dict (movements = movements))
        return plugin_appreport.REPORTPISA (html=html, title="my report")
        
    return dict(movements=movements, form=form)
    
def view_movs():
    movs_id=request.args(0)
    movs=db.movements[movs_id]
    
    return dict(movs=movs)    
    
def edit_movs():
    movs_id=request.args(0)
    movs=db.movements[movs_id]
    return dict (form=crud.update(db.movements, movs_id), movs=movs)    
    
def add_movs():
    form = crud.create(db.movements)
    return dict (form=form) 
    
def sell_parts():
    parts_id=request.args(0)
    parts=db.parts[parts_id]
    return dict(form=crud.update(db.parts,parts.id), parts=parts)
    
def gen_report():
    return dict(laptops = db(db.laptops.id>0).select())   
    
def gen_report_movs():
    return dict (movements = db(db.movements.id>0).select())     


       
 

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())



def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id[
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs bust be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

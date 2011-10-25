import zope.event

from plone.portlets.interfaces import IPortletAssignment
from zope.component import adapts
from zope.interface import implements
from zope.formlib import form
from zope.lifecycleevent import ObjectCreatedEvent

from .interfaces import ICollectivePortletClassLayer, ICollectivePortletClass

portletclass_field = ICollectivePortletClass['collective_portletclass']

def collective_portletclass__init__(self, context, request):
    # Patch the __init__ methods of portlet add and edit forms to append the
    # portletclass field.
    self.context = context
    self.request = request
    if ICollectivePortletClassLayer.providedBy(self.request):
        self.form_fields = self.form_fields + form.Fields(portletclass_field)

def collective_portletclass_createAndAdd(self, data):
    # Patch the createAndAdd method of portlet add forms to remove the
    # portletclass field from the assignment creation data, setting it manually.
    if ICollectivePortletClassLayer.providedBy(self.request):
        value = data[portletclass_field.__name__]
        del data[portletclass_field.__name__]
        ob = self.create(data)
        portletclass_field.set(ob, value)
    else:
        ob = self.create(data)
    zope.event.notify(ObjectCreatedEvent(ob))
    return self.add(ob)

class CollectivePortletClass(object):
    """Adapter to provide default value"""
    adapts(IPortletAssignment)
    implements(ICollectivePortletClass)

    def __init__(self, context):
        self.context = context

    @property
    def collective_portletclass(self):
        return getattr(self.context, 'collective_portletclass', u'')

    @collective_portletclass.setter
    def collective_portletclass(self, value):
        if value:
            setattr(self.context, 'collective_portletclass', value)
        elif getattr(self.context, 'collective_portletclass', None) is not None:
            del self.context.collective_portletclass

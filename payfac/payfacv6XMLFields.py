# ./payfacv6.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1ec446664fc53e0807eac7871cdc51ff2c72d72b
# Generated 2013-10-12 22:57:22.353020 by PyXB version 1.1.4
# Namespace http://psp.litle.com/api/merchant/onboard

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:53a5d178-33cc-11e3-a43e-68a86d4bf3ea')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://psp.litle.com/api/merchant/onboard', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120L))
STD_ANON._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxLength,
   STD_ANON._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON_._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_maxLength,
   STD_ANON_._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_2._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
STD_ANON_2._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_maxLength,
   STD_ANON_2._CF_minLength)

# Atomic SimpleTypeDefinition
class businessOverallScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessOverallScore')
    _Documentation = None
businessOverallScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessOverallScore, enum_prefix=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'0', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'10', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'20', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'30', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'40', tag=None)
businessOverallScore._CF_enumeration.addEnumeration(unicode_value=u'50', tag=None)
businessOverallScore._InitializeFacetMap(businessOverallScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'businessOverallScore', businessOverallScore)

# Atomic SimpleTypeDefinition
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_3._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_3._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_maxLength,
   STD_ANON_3._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_4 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_4._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_4._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_maxLength,
   STD_ANON_4._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_5._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
STD_ANON_5._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_maxLength,
   STD_ANON_5._CF_minLength)

# Atomic SimpleTypeDefinition
class nameAddressTaxIdAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameAddressTaxIdAssociationCode')
    _Documentation = None
nameAddressTaxIdAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nameAddressTaxIdAssociationCode, enum_prefix=None)
nameAddressTaxIdAssociationCode.NOT_VERIFIED = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NOT_VERIFIED', tag=u'NOT_VERIFIED')
nameAddressTaxIdAssociationCode.WRONG_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'WRONG_TAX_ID', tag=u'WRONG_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_OR_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_OR_ADDRESS', tag=u'NAME_OR_ADDRESS')
nameAddressTaxIdAssociationCode.BAD_NAME = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'BAD_NAME', tag=u'BAD_NAME')
nameAddressTaxIdAssociationCode.BAD_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'BAD_ADDRESS', tag=u'BAD_ADDRESS')
nameAddressTaxIdAssociationCode.MISSING_ADDRESS = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'MISSING_ADDRESS', tag=u'MISSING_ADDRESS')
nameAddressTaxIdAssociationCode.NAME_AND_ADDRESS_BAD_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_AND_ADDRESS_BAD_TAX_ID', tag=u'NAME_AND_ADDRESS_BAD_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_AND_ADDRESS_NO_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_AND_ADDRESS_NO_TAX_ID', tag=u'NAME_AND_ADDRESS_NO_TAX_ID')
nameAddressTaxIdAssociationCode.NAME_ADDRESS_TAX_ID = nameAddressTaxIdAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_TAX_ID', tag=u'NAME_ADDRESS_TAX_ID')
nameAddressTaxIdAssociationCode._InitializeFacetMap(nameAddressTaxIdAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nameAddressTaxIdAssociationCode', nameAddressTaxIdAssociationCode)

# Atomic SimpleTypeDefinition
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_6._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON_6._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_maxLength,
   STD_ANON_6._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_7._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9L))
STD_ANON_7._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_maxLength,
   STD_ANON_7._CF_minLength)

# Atomic SimpleTypeDefinition
class nameAddressSsnAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameAddressSsnAssociationCode')
    _Documentation = None
nameAddressSsnAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nameAddressSsnAssociationCode, enum_prefix=None)
nameAddressSsnAssociationCode.NOTHING = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NOTHING', tag=u'NOTHING')
nameAddressSsnAssociationCode.WRONG_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'WRONG_SSN', tag=u'WRONG_SSN')
nameAddressSsnAssociationCode.FIRST_LAST = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST', tag=u'FIRST_LAST')
nameAddressSsnAssociationCode.FIRST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_ADDRESS', tag=u'FIRST_ADDRESS')
nameAddressSsnAssociationCode.FIRST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_SSN', tag=u'FIRST_SSN')
nameAddressSsnAssociationCode.LAST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_ADDRESS', tag=u'LAST_ADDRESS')
nameAddressSsnAssociationCode.ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_SSN', tag=u'ADDRESS_SSN')
nameAddressSsnAssociationCode.LAST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_SSN', tag=u'LAST_SSN')
nameAddressSsnAssociationCode.FIRST_LAST_ADDRESS = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_ADDRESS', tag=u'FIRST_LAST_ADDRESS')
nameAddressSsnAssociationCode.FIRST_LAST_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_SSN', tag=u'FIRST_LAST_SSN')
nameAddressSsnAssociationCode.FIRST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_ADDRESS_SSN', tag=u'FIRST_ADDRESS_SSN')
nameAddressSsnAssociationCode.LAST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_ADDRESS_SSN', tag=u'LAST_ADDRESS_SSN')
nameAddressSsnAssociationCode.FIRST_LAST_ADDRESS_SSN = nameAddressSsnAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_ADDRESS_SSN', tag=u'FIRST_LAST_ADDRESS_SSN')
nameAddressSsnAssociationCode._InitializeFacetMap(nameAddressSsnAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'nameAddressSsnAssociationCode', nameAddressSsnAssociationCode)

# Atomic SimpleTypeDefinition
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_8._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_8._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_maxLength,
   STD_ANON_8._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_9._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_9._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_maxLength,
   STD_ANON_9._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_10._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(32L))
STD_ANON_10._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_maxLength,
   STD_ANON_10._CF_minLength)

# Atomic SimpleTypeDefinition
class businessToPrincipalScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessToPrincipalScore')
    _Documentation = None
businessToPrincipalScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessToPrincipalScore, enum_prefix=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'0', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'10', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'20', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'30', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'40', tag=None)
businessToPrincipalScore._CF_enumeration.addEnumeration(unicode_value=u'50', tag=None)
businessToPrincipalScore._InitializeFacetMap(businessToPrincipalScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'businessToPrincipalScore', businessToPrincipalScore)

# Atomic SimpleTypeDefinition
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_11._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_11._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_maxLength,
   STD_ANON_11._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_12 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_12._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5L))
STD_ANON_12._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_maxLength,
   STD_ANON_12._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_13 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_13._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
STD_ANON_13._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_maxLength,
   STD_ANON_13._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_14 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_14._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_14._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_maxLength,
   STD_ANON_14._CF_minLength)

# Atomic SimpleTypeDefinition
class principalNameAddressPhoneAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalNameAddressPhoneAssociationCode')
    _Documentation = None
principalNameAddressPhoneAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=principalNameAddressPhoneAssociationCode, enum_prefix=None)
principalNameAddressPhoneAssociationCode.NOTHING = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NOTHING', tag=u'NOTHING')
principalNameAddressPhoneAssociationCode.WRONG_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'WRONG_PHONE', tag=u'WRONG_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST', tag=u'FIRST_LAST')
principalNameAddressPhoneAssociationCode.FIRST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_ADDRESS', tag=u'FIRST_ADDRESS')
principalNameAddressPhoneAssociationCode.FIRST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_PHONE', tag=u'FIRST_PHONE')
principalNameAddressPhoneAssociationCode.LAST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_ADDRESS', tag=u'LAST_ADDRESS')
principalNameAddressPhoneAssociationCode.ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_PHONE', tag=u'ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.LAST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_PHONE', tag=u'LAST_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST_ADDRESS = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_ADDRESS', tag=u'FIRST_LAST_ADDRESS')
principalNameAddressPhoneAssociationCode.FIRST_LAST_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_PHONE', tag=u'FIRST_LAST_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_ADDRESS_PHONE', tag=u'FIRST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.LAST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'LAST_ADDRESS_PHONE', tag=u'LAST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode.FIRST_LAST_ADDRESS_PHONE = principalNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'FIRST_LAST_ADDRESS_PHONE', tag=u'FIRST_LAST_ADDRESS_PHONE')
principalNameAddressPhoneAssociationCode._InitializeFacetMap(principalNameAddressPhoneAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'principalNameAddressPhoneAssociationCode', principalNameAddressPhoneAssociationCode)

# Atomic SimpleTypeDefinition
class legalEntityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityType')
    _Documentation = None
legalEntityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=legalEntityType, enum_prefix=None)
legalEntityType.INDIVIDUAL_SOLE_PROPRIETORSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'INDIVIDUAL_SOLE_PROPRIETORSHIP', tag=u'INDIVIDUAL_SOLE_PROPRIETORSHIP')
legalEntityType.CORPORATION = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'CORPORATION', tag=u'CORPORATION')
legalEntityType.LIMITED_LIABILITY_COMPANY = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'LIMITED_LIABILITY_COMPANY', tag=u'LIMITED_LIABILITY_COMPANY')
legalEntityType.PARTNERSHIP = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'PARTNERSHIP', tag=u'PARTNERSHIP')
legalEntityType.ASSOCIATION_ESTATE_TRUST = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'ASSOCIATION_ESTATE_TRUST', tag=u'ASSOCIATION_ESTATE_TRUST')
legalEntityType.TAX_EXEMPT_ORGANIZATION = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'TAX_EXEMPT_ORGANIZATION', tag=u'TAX_EXEMPT_ORGANIZATION')
legalEntityType.INTERNATIONAL_ORGANIZATION = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'INTERNATIONAL_ORGANIZATION', tag=u'INTERNATIONAL_ORGANIZATION')
legalEntityType.GOVERNMENT_AGENCY = legalEntityType._CF_enumeration.addEnumeration(unicode_value=u'GOVERNMENT_AGENCY', tag=u'GOVERNMENT_AGENCY')
legalEntityType._InitializeFacetMap(legalEntityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'legalEntityType', legalEntityType)

# Atomic SimpleTypeDefinition
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_15._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_15._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_maxLength,
   STD_ANON_15._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_16._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
STD_ANON_16._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_maxLength,
   STD_ANON_16._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_17 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_17._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_17._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_maxLength,
   STD_ANON_17._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_18 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_18._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9L))
STD_ANON_18._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_maxLength,
   STD_ANON_18._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_19 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_19._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_19._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_maxLength,
   STD_ANON_19._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_20 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_20._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_20._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_maxLength,
   STD_ANON_20._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_21 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_21._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
STD_ANON_21._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_maxLength,
   STD_ANON_21._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_22 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_22._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_22._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_maxLength,
   STD_ANON_22._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_23 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_23._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
STD_ANON_23._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_maxLength,
   STD_ANON_23._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_24 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_24._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_24._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_maxLength,
   STD_ANON_24._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_25 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_25._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
STD_ANON_25._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_maxLength,
   STD_ANON_25._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_26 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_26._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
STD_ANON_26._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_maxLength,
   STD_ANON_26._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_27 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_27._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_27._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_maxLength,
   STD_ANON_27._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_28 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_28._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_28._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_maxLength,
   STD_ANON_28._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_29 (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_29._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_29, value=pyxb.binding.datatypes.int(4))
STD_ANON_29._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_29, value=pyxb.binding.datatypes.int(1))
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_maxInclusive,
   STD_ANON_29._CF_minInclusive)

# Atomic SimpleTypeDefinition
class STD_ANON_30 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_30._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_30._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_maxLength,
   STD_ANON_30._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_31 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_31._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_31._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_maxLength,
   STD_ANON_31._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_32 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_32._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
STD_ANON_32._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_maxLength,
   STD_ANON_32._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_33 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_33._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5L))
STD_ANON_33._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_33._InitializeFacetMap(STD_ANON_33._CF_maxLength,
   STD_ANON_33._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_34 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_34._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
STD_ANON_34._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_34._InitializeFacetMap(STD_ANON_34._CF_maxLength,
   STD_ANON_34._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_35 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_35._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_35._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_35._InitializeFacetMap(STD_ANON_35._CF_maxLength,
   STD_ANON_35._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_36 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_36._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
STD_ANON_36._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_36._InitializeFacetMap(STD_ANON_36._CF_maxLength,
   STD_ANON_36._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_37 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_37._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_37._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_37._InitializeFacetMap(STD_ANON_37._CF_maxLength,
   STD_ANON_37._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_38 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_38._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_38._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_38._InitializeFacetMap(STD_ANON_38._CF_maxLength,
   STD_ANON_38._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_39 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_39._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
STD_ANON_39._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_39._InitializeFacetMap(STD_ANON_39._CF_maxLength,
   STD_ANON_39._CF_minLength)

# Atomic SimpleTypeDefinition
class principalOverallScore (pyxb.binding.datatypes.int, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalOverallScore')
    _Documentation = None
principalOverallScore._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=principalOverallScore, enum_prefix=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'0', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'10', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'20', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'30', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'40', tag=None)
principalOverallScore._CF_enumeration.addEnumeration(unicode_value=u'50', tag=None)
principalOverallScore._InitializeFacetMap(principalOverallScore._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'principalOverallScore', principalOverallScore)

# Atomic SimpleTypeDefinition
class STD_ANON_40 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
STD_ANON_40._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_40._InitializeFacetMap(STD_ANON_40._CF_maxLength,
   STD_ANON_40._CF_minLength)

# Atomic SimpleTypeDefinition
class businessNameAddressPhoneAssociationCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessNameAddressPhoneAssociationCode')
    _Documentation = None
businessNameAddressPhoneAssociationCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=businessNameAddressPhoneAssociationCode, enum_prefix=None)
businessNameAddressPhoneAssociationCode.NOT_VERIFIED = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NOT_VERIFIED', tag=u'NOT_VERIFIED')
businessNameAddressPhoneAssociationCode.WRONG_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'WRONG_PHONE', tag=u'WRONG_PHONE')
businessNameAddressPhoneAssociationCode.NAME_OR_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_OR_ADDRESS', tag=u'NAME_OR_ADDRESS')
businessNameAddressPhoneAssociationCode.BAD_NAME = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'BAD_NAME', tag=u'BAD_NAME')
businessNameAddressPhoneAssociationCode.BAD_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'BAD_ADDRESS', tag=u'BAD_ADDRESS')
businessNameAddressPhoneAssociationCode.MISSING_ADDRESS = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'MISSING_ADDRESS', tag=u'MISSING_ADDRESS')
businessNameAddressPhoneAssociationCode.NAME_AND_ADDRESS_BAD_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_AND_ADDRESS_BAD_PHONE', tag=u'NAME_AND_ADDRESS_BAD_PHONE')
businessNameAddressPhoneAssociationCode.NAME_AND_ADDRESS_NO_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_AND_ADDRESS_NO_PHONE', tag=u'NAME_AND_ADDRESS_NO_PHONE')
businessNameAddressPhoneAssociationCode.NAME_ADDRESS_PHONE = businessNameAddressPhoneAssociationCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_PHONE', tag=u'NAME_ADDRESS_PHONE')
businessNameAddressPhoneAssociationCode._InitializeFacetMap(businessNameAddressPhoneAssociationCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'businessNameAddressPhoneAssociationCode', businessNameAddressPhoneAssociationCode)

# Atomic SimpleTypeDefinition
class STD_ANON_41 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_41._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
STD_ANON_41._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_41._InitializeFacetMap(STD_ANON_41._CF_maxLength,
   STD_ANON_41._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_42 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_42._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
STD_ANON_42._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_42._InitializeFacetMap(STD_ANON_42._CF_maxLength,
   STD_ANON_42._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_43 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_43._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_43._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_43._InitializeFacetMap(STD_ANON_43._CF_maxLength,
   STD_ANON_43._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_44 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_44._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(120L))
STD_ANON_44._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_44._InitializeFacetMap(STD_ANON_44._CF_maxLength,
   STD_ANON_44._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_45 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_45._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_45._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_45._InitializeFacetMap(STD_ANON_45._CF_maxLength,
   STD_ANON_45._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_46 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_46._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
STD_ANON_46._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_46._InitializeFacetMap(STD_ANON_46._CF_maxLength,
   STD_ANON_46._CF_minLength)

# Atomic SimpleTypeDefinition
class riskIndicatorCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'riskIndicatorCode')
    _Documentation = None
riskIndicatorCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=riskIndicatorCode, enum_prefix=None)
riskIndicatorCode.UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNKNOWN', tag=u'UNKNOWN')
riskIndicatorCode.SSN_DECEASED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_DECEASED', tag=u'SSN_DECEASED')
riskIndicatorCode.SSN_PRIOR_TO_DOB = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_PRIOR_TO_DOB', tag=u'SSN_PRIOR_TO_DOB')
riskIndicatorCode.SSN_ADDRESS_PHONE_NOT_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_ADDRESS_PHONE_NOT_MATCH', tag=u'SSN_ADDRESS_PHONE_NOT_MATCH')
riskIndicatorCode.SSN_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_INVALID', tag=u'SSN_INVALID')
riskIndicatorCode.PHONE_NUMBER_DISCONNECTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_DISCONNECTED', tag=u'PHONE_NUMBER_DISCONNECTED')
riskIndicatorCode.PHONE_NUMBER_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_INVALID', tag=u'PHONE_NUMBER_INVALID')
riskIndicatorCode.PHONE_NUMBER_PAGER = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_PAGER', tag=u'PHONE_NUMBER_PAGER')
riskIndicatorCode.PHONE_NUMBER_MOBILE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_MOBILE', tag=u'PHONE_NUMBER_MOBILE')
riskIndicatorCode.ADDRESS_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_INVALID', tag=u'ADDRESS_INVALID')
riskIndicatorCode.ZIP_BELONGS_POST_OFFICE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ZIP_BELONGS_POST_OFFICE', tag=u'ZIP_BELONGS_POST_OFFICE')
riskIndicatorCode.ADDRESS_INVALID_APARTMENT_DESIGNATION = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_INVALID_APARTMENT_DESIGNATION', tag=u'ADDRESS_INVALID_APARTMENT_DESIGNATION')
riskIndicatorCode.ADDRESS_COMMERCIAL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_COMMERCIAL', tag=u'ADDRESS_COMMERCIAL')
riskIndicatorCode.PHONE_NUMBER_COMMERCIAL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_COMMERCIAL', tag=u'PHONE_NUMBER_COMMERCIAL')
riskIndicatorCode.PHONE_NUMBER_ZIP_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_ZIP_INVALID', tag=u'PHONE_NUMBER_ZIP_INVALID')
riskIndicatorCode.UNABLE_TO_VERIFY_NAS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_NAS', tag=u'UNABLE_TO_VERIFY_NAS')
riskIndicatorCode.UNABLE_TO_VERIFY_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_ADDRESS', tag=u'UNABLE_TO_VERIFY_ADDRESS')
riskIndicatorCode.UNABLE_TO_VERIFY_SSN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_SSN', tag=u'UNABLE_TO_VERIFY_SSN')
riskIndicatorCode.UNABLE_TO_VERIFY_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_PHONE', tag=u'UNABLE_TO_VERIFY_PHONE')
riskIndicatorCode.UNABLE_TO_VERIFY_DOB = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_DOB', tag=u'UNABLE_TO_VERIFY_DOB')
riskIndicatorCode.SSN_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_MISKEYED', tag=u'SSN_MISKEYED')
riskIndicatorCode.ADDRESS_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_MISKEYED', tag=u'ADDRESS_MISKEYED')
riskIndicatorCode.PHONE_NUMBER_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_MISKEYED', tag=u'PHONE_NUMBER_MISKEYED')
riskIndicatorCode.NAME_MATCHES_OFAC = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_MATCHES_OFAC', tag=u'NAME_MATCHES_OFAC')
riskIndicatorCode.UNABLE_TO_VERIFY_NAME = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_NAME', tag=u'UNABLE_TO_VERIFY_NAME')
riskIndicatorCode.SSN_MATCHES_MULTI_NAMES = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_MATCHES_MULTI_NAMES', tag=u'SSN_MATCHES_MULTI_NAMES')
riskIndicatorCode.SSN_RECENTLY_ISSUED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_RECENTLY_ISSUED', tag=u'SSN_RECENTLY_ISSUED')
riskIndicatorCode.ZIP_CORPORATE_MILITARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ZIP_CORPORATE_MILITARY', tag=u'ZIP_CORPORATE_MILITARY')
riskIndicatorCode.DLL_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DLL_INVALID', tag=u'DLL_INVALID')
riskIndicatorCode.NAME_ADDRESS_MATCH_BANKRUPTCY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_MATCH_BANKRUPTCY', tag=u'NAME_ADDRESS_MATCH_BANKRUPTCY')
riskIndicatorCode.PHONE_AREA_CODE_CHANGING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_AREA_CODE_CHANGING', tag=u'PHONE_AREA_CODE_CHANGING')
riskIndicatorCode.WORK_PHONE_PAGER = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'WORK_PHONE_PAGER', tag=u'WORK_PHONE_PAGER')
riskIndicatorCode.UNABLE_TO_VERIFY_FIRST_NAME = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_FIRST_NAME', tag=u'UNABLE_TO_VERIFY_FIRST_NAME')
riskIndicatorCode.PHONE_ADDRESS_DISTANT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_ADDRESS_DISTANT', tag=u'PHONE_ADDRESS_DISTANT')
riskIndicatorCode.ADDRESS_MATCHES_PRISON = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_MATCHES_PRISON', tag=u'ADDRESS_MATCHES_PRISON')
riskIndicatorCode.SSN_LAST_NAME_NO_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_LAST_NAME_NO_MATCH', tag=u'SSN_LAST_NAME_NO_MATCH')
riskIndicatorCode.SSN_FIRST_NAME_NO_MATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_FIRST_NAME_NO_MATCH', tag=u'SSN_FIRST_NAME_NO_MATCH')
riskIndicatorCode.WORK_HOME_PHONE_DISTANT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'WORK_HOME_PHONE_DISTANT', tag=u'WORK_HOME_PHONE_DISTANT')
riskIndicatorCode.NAME_ADDRESS_TIN_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_TIN_MISMATCH', tag=u'NAME_ADDRESS_TIN_MISMATCH')
riskIndicatorCode.WORK_PHONE_INVALID = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'WORK_PHONE_INVALID', tag=u'WORK_PHONE_INVALID')
riskIndicatorCode.WORK_PHONE_DISCONNECTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'WORK_PHONE_DISCONNECTED', tag=u'WORK_PHONE_DISCONNECTED')
riskIndicatorCode.WORK_PHONE_MOBILE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'WORK_PHONE_MOBILE', tag=u'WORK_PHONE_MOBILE')
riskIndicatorCode.ADDRESS_RETURNS_DIFF_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_RETURNS_DIFF_PHONE', tag=u'ADDRESS_RETURNS_DIFF_PHONE')
riskIndicatorCode.SSN_LNAME_NOT_MATCHED_FNAME_MATCHED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_LNAME_NOT_MATCHED_FNAME_MATCHED', tag=u'SSN_LNAME_NOT_MATCHED_FNAME_MATCHED')
riskIndicatorCode.PHONE_RESIDENTIAL_LISTING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_RESIDENTIAL_LISTING', tag=u'PHONE_RESIDENTIAL_LISTING')
riskIndicatorCode.SINGLE_FAMILY_DWELLING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SINGLE_FAMILY_DWELLING', tag=u'SINGLE_FAMILY_DWELLING')
riskIndicatorCode.SSN_NOT_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_NOT_FOUND', tag=u'SSN_NOT_FOUND')
riskIndicatorCode.SSN_BELONGS_TO_DIFF_NAME_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_BELONGS_TO_DIFF_NAME_ADDRESS', tag=u'SSN_BELONGS_TO_DIFF_NAME_ADDRESS')
riskIndicatorCode.PHONE_BELONGS_TO_DIFF_NAME_ADDRESS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_BELONGS_TO_DIFF_NAME_ADDRESS', tag=u'PHONE_BELONGS_TO_DIFF_NAME_ADDRESS')
riskIndicatorCode.NAME_ADDRESS_UNLISTED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_UNLISTED', tag=u'NAME_ADDRESS_UNLISTED')
riskIndicatorCode.NAME_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_MISKEYED', tag=u'NAME_MISKEYED')
riskIndicatorCode.NAME_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_MISSING', tag=u'NAME_MISSING')
riskIndicatorCode.ADDRESS_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_MISSING', tag=u'ADDRESS_MISSING')
riskIndicatorCode.SSN_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_MISSING', tag=u'SSN_MISSING')
riskIndicatorCode.PHONE_NUMBER_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'PHONE_NUMBER_MISSING', tag=u'PHONE_NUMBER_MISSING')
riskIndicatorCode.DOB_MISSING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DOB_MISSING', tag=u'DOB_MISSING')
riskIndicatorCode.NAME_ADDRESS_RETURN_DIFF_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_RETURN_DIFF_PHONE', tag=u'NAME_ADDRESS_RETURN_DIFF_PHONE')
riskIndicatorCode.DOB_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DOB_MISKEYED', tag=u'DOB_MISKEYED')
riskIndicatorCode.SSN_NON_US_CITIZEN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_NON_US_CITIZEN', tag=u'SSN_NON_US_CITIZEN')
riskIndicatorCode.ALTERNATE_BUSINESS_NAME_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ALTERNATE_BUSINESS_NAME_FOUND', tag=u'ALTERNATE_BUSINESS_NAME_FOUND')
riskIndicatorCode.DBA_MATCH_PUBLIC_RECORDS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DBA_MATCH_PUBLIC_RECORDS', tag=u'DBA_MATCH_PUBLIC_RECORDS')
riskIndicatorCode.SSN_RECENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_RECENT', tag=u'SSN_RECENT')
riskIndicatorCode.SSN_TOO_OLD = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_TOO_OLD', tag=u'SSN_TOO_OLD')
riskIndicatorCode.TIN_NAME_ADDRESS_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'TIN_NAME_ADDRESS_MISMATCH', tag=u'TIN_NAME_ADDRESS_MISMATCH')
riskIndicatorCode.BUSINESS_NOT_IN_GOOD_STANDING = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'BUSINESS_NOT_IN_GOOD_STANDING', tag=u'BUSINESS_NOT_IN_GOOD_STANDING')
riskIndicatorCode.NAME_ADDRESS_MATCH_JUDGMENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_ADDRESS_MATCH_JUDGMENT', tag=u'NAME_ADDRESS_MATCH_JUDGMENT')
riskIndicatorCode.BUSINESS_INACTIVE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'BUSINESS_INACTIVE', tag=u'BUSINESS_INACTIVE')
riskIndicatorCode.NO_UPDATE_IN_LAST_THREE_YEARS = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NO_UPDATE_IN_LAST_THREE_YEARS', tag=u'NO_UPDATE_IN_LAST_THREE_YEARS')
riskIndicatorCode.SSN_NOT_PRIMARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_NOT_PRIMARY', tag=u'SSN_NOT_PRIMARY')
riskIndicatorCode.ZIP_CORP_ONLY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ZIP_CORP_ONLY', tag=u'ZIP_CORP_ONLY')
riskIndicatorCode.ADDRESS_MISMATCH = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_MISMATCH', tag=u'ADDRESS_MISMATCH')
riskIndicatorCode.DL_DIFFERENT = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DL_DIFFERENT', tag=u'DL_DIFFERENT')
riskIndicatorCode.DL_NOT_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DL_NOT_FOUND', tag=u'DL_NOT_FOUND')
riskIndicatorCode.DL_MISKEYED = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'DL_MISKEYED', tag=u'DL_MISKEYED')
riskIndicatorCode.UNABLE_TO_VERIFY_DL = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_DL', tag=u'UNABLE_TO_VERIFY_DL')
riskIndicatorCode.SSN_INVALID_SSA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_INVALID_SSA', tag=u'SSN_INVALID_SSA')
riskIndicatorCode.SSN_IS_ITIN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_IS_ITIN', tag=u'SSN_IS_ITIN')
riskIndicatorCode.SSN_MULTI_IDENTITY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_MULTI_IDENTITY', tag=u'SSN_MULTI_IDENTITY')
riskIndicatorCode.ZIP_MILITARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ZIP_MILITARY', tag=u'ZIP_MILITARY')
riskIndicatorCode.MULTIPLE_SSN_FOUND = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'MULTIPLE_SSN_FOUND', tag=u'MULTIPLE_SSN_FOUND')
riskIndicatorCode.ADDRESS_DISCREPANCY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_DISCREPANCY', tag=u'ADDRESS_DISCREPANCY')
riskIndicatorCode.ADDRESS_PO_BOX = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_PO_BOX', tag=u'ADDRESS_PO_BOX')
riskIndicatorCode.SSN_RANDOM_SSA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'SSN_RANDOM_SSA', tag=u'SSN_RANDOM_SSA')
riskIndicatorCode.ADDRESS_MISMATCH_SECONDARY = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'ADDRESS_MISMATCH_SECONDARY', tag=u'ADDRESS_MISMATCH_SECONDARY')
riskIndicatorCode.NAME_MATCHES_NON_OFAC = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'NAME_MATCHES_NON_OFAC', tag=u'NAME_MATCHES_NON_OFAC')
riskIndicatorCode.UNABLE_TO_VERIFY_ZIP_CODE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'UNABLE_TO_VERIFY_ZIP_CODE', tag=u'UNABLE_TO_VERIFY_ZIP_CODE')
riskIndicatorCode.IP_ADDRESS_UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_UNKNOWN', tag=u'IP_ADDRESS_UNKNOWN')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_STATE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_DIFFERENT_STATE', tag=u'IP_ADDRESS_DIFFERENT_STATE')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_ZIP = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_DIFFERENT_ZIP', tag=u'IP_ADDRESS_DIFFERENT_ZIP')
riskIndicatorCode.IP_ADDRESS_DIFFERENT_PHONE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_DIFFERENT_PHONE', tag=u'IP_ADDRESS_DIFFERENT_PHONE')
riskIndicatorCode.IP_ADDRESS_DOMAIN_UNKNOWN = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_DOMAIN_UNKNOWN', tag=u'IP_ADDRESS_DOMAIN_UNKNOWN')
riskIndicatorCode.IP_ADDRESS_NOT_ASSIGNED_TO_USA = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_NOT_ASSIGNED_TO_USA', tag=u'IP_ADDRESS_NOT_ASSIGNED_TO_USA')
riskIndicatorCode.IP_ADDRESS_NON_ROUTABLE = riskIndicatorCode._CF_enumeration.addEnumeration(unicode_value=u'IP_ADDRESS_NON_ROUTABLE', tag=u'IP_ADDRESS_NON_ROUTABLE')
riskIndicatorCode._InitializeFacetMap(riskIndicatorCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'riskIndicatorCode', riskIndicatorCode)

# Atomic SimpleTypeDefinition
class STD_ANON_47 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_47._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16L))
STD_ANON_47._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_47._InitializeFacetMap(STD_ANON_47._CF_maxLength,
   STD_ANON_47._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_48 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_48._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
STD_ANON_48._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_48._InitializeFacetMap(STD_ANON_48._CF_maxLength,
   STD_ANON_48._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_49 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_49._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_49._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_49._InitializeFacetMap(STD_ANON_49._CF_maxLength,
   STD_ANON_49._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_50 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_50._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
STD_ANON_50._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_50._InitializeFacetMap(STD_ANON_50._CF_maxLength,
   STD_ANON_50._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_51 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_51._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
STD_ANON_51._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_51._InitializeFacetMap(STD_ANON_51._CF_maxLength,
   STD_ANON_51._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_52 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_52._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
STD_ANON_52._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_52._InitializeFacetMap(STD_ANON_52._CF_maxLength,
   STD_ANON_52._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_53 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_53._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_53._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_53._InitializeFacetMap(STD_ANON_53._CF_maxLength,
   STD_ANON_53._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_54 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_54._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON_54._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_54._InitializeFacetMap(STD_ANON_54._CF_maxLength,
   STD_ANON_54._CF_minLength)

# Atomic SimpleTypeDefinition
class STD_ANON_55 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON_55._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
STD_ANON_55._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
STD_ANON_55._InitializeFacetMap(STD_ANON_55._CF_maxLength,
   STD_ANON_55._CF_minLength)

# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}paypageCredential uses Python identifier paypageCredential
    __paypageCredential = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential'), 'paypageCredential', '__httppsp_litle_comapimerchantonboard_CTD_ANON_httppsp_litle_comapimerchantonboardpaypageCredential', True)


    paypageCredential = property(__paypageCredential.value, __paypageCredential.set, None, None)


    _ElementMap = {
        __paypageCredential.name() : __paypageCredential
    }
    _AttributeMap = {

    }



# Complex type principalAddressUpdatable with content type ELEMENT_ONLY
class principalAddressUpdatable (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalAddressUpdatable')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httppsp_litle_comapimerchantonboard_principalAddressUpdatable_httppsp_litle_comapimerchantonboardcity', False)


    city = property(__city.value, __city.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), 'streetAddress2', '__httppsp_litle_comapimerchantonboard_principalAddressUpdatable_httppsp_litle_comapimerchantonboardstreetAddress2', False)


    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'stateProvince'), 'stateProvince', '__httppsp_litle_comapimerchantonboard_principalAddressUpdatable_httppsp_litle_comapimerchantonboardstateProvince', False)


    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), 'streetAddress1', '__httppsp_litle_comapimerchantonboard_principalAddressUpdatable_httppsp_litle_comapimerchantonboardstreetAddress1', False)


    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), 'postalCode', '__httppsp_litle_comapimerchantonboard_principalAddressUpdatable_httppsp_litle_comapimerchantonboardpostalCode', False)


    postalCode = property(__postalCode.value, __postalCode.set, None, None)


    _ElementMap = {
        __city.name() : __city,
        __streetAddress2.name() : __streetAddress2,
        __stateProvince.name() : __stateProvince,
        __streetAddress1.name() : __streetAddress1,
        __postalCode.name() : __postalCode
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalAddressUpdatable', principalAddressUpdatable)


# Complex type response_ with content type ELEMENT_ONLY
class response_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'response')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), 'transactionId', '__httppsp_litle_comapimerchantonboard_response__httppsp_litle_comapimerchantonboardtransactionId', False)


    transactionId = property(__transactionId.value, __transactionId.set, None, None)


    _ElementMap = {
        __transactionId.name() : __transactionId
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'response', response_)


# Complex type errorResponse_ with content type ELEMENT_ONLY
class errorResponse_ (response_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'errorResponse')
    # Base type is response_

    # Element {http://psp.litle.com/api/merchant/onboard}errors uses Python identifier errors
    __errors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errors'), 'errors', '__httppsp_litle_comapimerchantonboard_errorResponse__httppsp_litle_comapimerchantonboarderrors', False)


    errors = property(__errors.value, __errors.set, None, None)


    # Element transactionId ({http://psp.litle.com/api/merchant/onboard}transactionId) inherited from {http://psp.litle.com/api/merchant/onboard}response

    _ElementMap = response_._ElementMap.copy()
    _ElementMap.update({
        __errors.name() : __errors
    })
    _AttributeMap = response_._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'errorResponse', errorResponse_)


# Complex type principalVerificationIndicators with content type ELEMENT_ONLY
class principalVerificationIndicators (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalVerificationIndicators')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}phoneVerified uses Python identifier phoneVerified
    __phoneVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified'), 'phoneVerified', '__httppsp_litle_comapimerchantonboard_principalVerificationIndicators_httppsp_litle_comapimerchantonboardphoneVerified', False)


    phoneVerified = property(__phoneVerified.value, __phoneVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}dobVerified uses Python identifier dobVerified
    __dobVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dobVerified'), 'dobVerified', '__httppsp_litle_comapimerchantonboard_principalVerificationIndicators_httppsp_litle_comapimerchantonboarddobVerified', False)


    dobVerified = property(__dobVerified.value, __dobVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameVerified uses Python identifier nameVerified
    __nameVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameVerified'), 'nameVerified', '__httppsp_litle_comapimerchantonboard_principalVerificationIndicators_httppsp_litle_comapimerchantonboardnameVerified', False)


    nameVerified = property(__nameVerified.value, __nameVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}addressVerified uses Python identifier addressVerified
    __addressVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressVerified'), 'addressVerified', '__httppsp_litle_comapimerchantonboard_principalVerificationIndicators_httppsp_litle_comapimerchantonboardaddressVerified', False)


    addressVerified = property(__addressVerified.value, __addressVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}ssnVerified uses Python identifier ssnVerified
    __ssnVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ssnVerified'), 'ssnVerified', '__httppsp_litle_comapimerchantonboard_principalVerificationIndicators_httppsp_litle_comapimerchantonboardssnVerified', False)


    ssnVerified = property(__ssnVerified.value, __ssnVerified.set, None, None)


    _ElementMap = {
        __phoneVerified.name() : __phoneVerified,
        __dobVerified.name() : __dobVerified,
        __nameVerified.name() : __nameVerified,
        __addressVerified.name() : __addressVerified,
        __ssnVerified.name() : __ssnVerified
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalVerificationIndicators', principalVerificationIndicators)


# Complex type CTD_ANON_ with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}paypageCredential uses Python identifier paypageCredential
    __paypageCredential = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential'), 'paypageCredential', '__httppsp_litle_comapimerchantonboard_CTD_ANON__httppsp_litle_comapimerchantonboardpaypageCredential', True)


    paypageCredential = property(__paypageCredential.value, __paypageCredential.set, None, None)


    _ElementMap = {
        __paypageCredential.name() : __paypageCredential
    }
    _AttributeMap = {

    }



# Complex type principalAddress with content type ELEMENT_ONLY
class principalAddress (principalAddressUpdatable):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalAddress')
    # Base type is principalAddressUpdatable

    # Element postalCode ({http://psp.litle.com/api/merchant/onboard}postalCode) inherited from {http://psp.litle.com/api/merchant/onboard}principalAddressUpdatable

    # Element city ({http://psp.litle.com/api/merchant/onboard}city) inherited from {http://psp.litle.com/api/merchant/onboard}principalAddressUpdatable

    # Element streetAddress1 ({http://psp.litle.com/api/merchant/onboard}streetAddress1) inherited from {http://psp.litle.com/api/merchant/onboard}principalAddressUpdatable

    # Element stateProvince ({http://psp.litle.com/api/merchant/onboard}stateProvince) inherited from {http://psp.litle.com/api/merchant/onboard}principalAddressUpdatable

    # Element {http://psp.litle.com/api/merchant/onboard}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'countryCode'), 'countryCode', '__httppsp_litle_comapimerchantonboard_principalAddress_httppsp_litle_comapimerchantonboardcountryCode', False)


    countryCode = property(__countryCode.value, __countryCode.set, None, None)


    # Element streetAddress2 ({http://psp.litle.com/api/merchant/onboard}streetAddress2) inherited from {http://psp.litle.com/api/merchant/onboard}principalAddressUpdatable

    _ElementMap = principalAddressUpdatable._ElementMap.copy()
    _ElementMap.update({
        __countryCode.name() : __countryCode
    })
    _AttributeMap = principalAddressUpdatable._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'principalAddress', principalAddress)


# Complex type backgroundCheckResults_ with content type ELEMENT_ONLY
class backgroundCheckResults_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}backgroundCheckDecisionNotes uses Python identifier backgroundCheckDecisionNotes
    __backgroundCheckDecisionNotes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckDecisionNotes'), 'backgroundCheckDecisionNotes', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardbackgroundCheckDecisionNotes', False)


    backgroundCheckDecisionNotes = property(__backgroundCheckDecisionNotes.value, __backgroundCheckDecisionNotes.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}lienResult uses Python identifier lienResult
    __lienResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lienResult'), 'lienResult', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardlienResult', False)


    lienResult = property(__lienResult.value, __lienResult.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}business uses Python identifier business
    __business = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'business'), 'business', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardbusiness', False)


    business = property(__business.value, __business.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principal'), 'principal', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardprincipal', False)


    principal = property(__principal.value, __principal.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankruptcyData uses Python identifier bankruptcyData
    __bankruptcyData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyData'), 'bankruptcyData', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardbankruptcyData', False)


    bankruptcyData = property(__bankruptcyData.value, __bankruptcyData.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}businessToPrincipalAssociation uses Python identifier businessToPrincipalAssociation
    __businessToPrincipalAssociation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'businessToPrincipalAssociation'), 'businessToPrincipalAssociation', '__httppsp_litle_comapimerchantonboard_backgroundCheckResults__httppsp_litle_comapimerchantonboardbusinessToPrincipalAssociation', False)


    businessToPrincipalAssociation = property(__businessToPrincipalAssociation.value, __businessToPrincipalAssociation.set, None, None)


    _ElementMap = {
        __backgroundCheckDecisionNotes.name() : __backgroundCheckDecisionNotes,
        __lienResult.name() : __lienResult,
        __business.name() : __business,
        __principal.name() : __principal,
        __bankruptcyData.name() : __bankruptcyData,
        __businessToPrincipalAssociation.name() : __businessToPrincipalAssociation
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'backgroundCheckResults', backgroundCheckResults_)


# Complex type legalEntityCreateRequest_ with content type ELEMENT_ONLY
class legalEntityCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityCreateRequest')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}taxId uses Python identifier taxId
    __taxId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxId'), 'taxId', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardtaxId', False)


    taxId = property(__taxId.value, __taxId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}hasAcceptedCreditCards uses Python identifier hasAcceptedCreditCards
    __hasAcceptedCreditCards = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards'), 'hasAcceptedCreditCards', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardhasAcceptedCreditCards', False)


    hasAcceptedCreditCards = property(__hasAcceptedCreditCards.value, __hasAcceptedCreditCards.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'address'), 'address', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardaddress', False)


    address = property(__address.value, __address.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}legalEntityType uses Python identifier legalEntityType
    __legalEntityType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legalEntityType'), 'legalEntityType', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardlegalEntityType', False)


    legalEntityType = property(__legalEntityType.value, __legalEntityType.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), 'contactPhone', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardcontactPhone', False)


    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}PCI uses Python identifier PCI
    __PCI = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PCI'), 'PCI', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardPCI', False)


    PCI = property(__PCI.value, __PCI.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}doingBusinessAs uses Python identifier doingBusinessAs
    __doingBusinessAs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs'), 'doingBusinessAs', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboarddoingBusinessAs', False)


    doingBusinessAs = property(__doingBusinessAs.value, __doingBusinessAs.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}legalEntityName uses Python identifier legalEntityName
    __legalEntityName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legalEntityName'), 'legalEntityName', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardlegalEntityName', False)


    legalEntityName = property(__legalEntityName.value, __legalEntityName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}annualCreditCardSalesVolume uses Python identifier annualCreditCardSalesVolume
    __annualCreditCardSalesVolume = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume'), 'annualCreditCardSalesVolume', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardannualCreditCardSalesVolume', False)


    annualCreditCardSalesVolume = property(__annualCreditCardSalesVolume.value, __annualCreditCardSalesVolume.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}principals uses Python identifier principals
    __principals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principals'), 'principals', '__httppsp_litle_comapimerchantonboard_legalEntityCreateRequest__httppsp_litle_comapimerchantonboardprincipals', False)


    principals = property(__principals.value, __principals.set, None, None)


    _ElementMap = {
        __taxId.name() : __taxId,
        __hasAcceptedCreditCards.name() : __hasAcceptedCreditCards,
        __address.name() : __address,
        __legalEntityType.name() : __legalEntityType,
        __contactPhone.name() : __contactPhone,
        __PCI.name() : __PCI,
        __doingBusinessAs.name() : __doingBusinessAs,
        __legalEntityName.name() : __legalEntityName,
        __annualCreditCardSalesVolume.name() : __annualCreditCardSalesVolume,
        __principals.name() : __principals
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityCreateRequest', legalEntityCreateRequest_)


# Complex type legalEntityCreateResponse_ with content type ELEMENT_ONLY
class legalEntityCreateResponse_ (response_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityCreateResponse')
    # Base type is response_

    # Element {http://psp.litle.com/api/merchant/onboard}backgroundCheckResults uses Python identifier backgroundCheckResults
    __backgroundCheckResults = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults'), 'backgroundCheckResults', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardbackgroundCheckResults', False)


    backgroundCheckResults = property(__backgroundCheckResults.value, __backgroundCheckResults.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), 'responseCode', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardresponseCode', False)


    responseCode = property(__responseCode.value, __responseCode.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId'), 'legalEntityId', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardlegalEntityId', False)


    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}principals uses Python identifier principals
    __principals = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principals'), 'principals', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardprincipals', False)


    principals = property(__principals.value, __principals.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseDescription'), 'responseDescription', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardresponseDescription', False)


    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)


    # Element transactionId ({http://psp.litle.com/api/merchant/onboard}transactionId) inherited from {http://psp.litle.com/api/merchant/onboard}response

    # Element {http://psp.litle.com/api/merchant/onboard}originalLegalEntity uses Python identifier originalLegalEntity
    __originalLegalEntity = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalLegalEntity'), 'originalLegalEntity', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__httppsp_litle_comapimerchantonboardoriginalLegalEntity', False)


    originalLegalEntity = property(__originalLegalEntity.value, __originalLegalEntity.set, None, None)


    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httppsp_litle_comapimerchantonboard_legalEntityCreateResponse__duplicate', pyxb.binding.datatypes.boolean)

    duplicate = property(__duplicate.value, __duplicate.set, None, None)


    _ElementMap = response_._ElementMap.copy()
    _ElementMap.update({
        __backgroundCheckResults.name() : __backgroundCheckResults,
        __responseCode.name() : __responseCode,
        __legalEntityId.name() : __legalEntityId,
        __principals.name() : __principals,
        __responseDescription.name() : __responseDescription,
        __originalLegalEntity.name() : __originalLegalEntity
    })
    _AttributeMap = response_._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })
Namespace.addCategoryObject('typeBinding', u'legalEntityCreateResponse', legalEntityCreateResponse_)


# Complex type potentialRiskIndicator with content type ELEMENT_ONLY
class potentialRiskIndicator (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'potentialRiskIndicator')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_potentialRiskIndicator_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httppsp_litle_comapimerchantonboard_potentialRiskIndicator_httppsp_litle_comapimerchantonboardcode', False)


    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __code.name() : __code
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'potentialRiskIndicator', potentialRiskIndicator)


# Complex type legalEntityPrincipalUpdatable_ with content type ELEMENT_ONLY
class legalEntityPrincipalUpdatable_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityPrincipalUpdatable')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), 'contactPhone', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalUpdatable__httppsp_litle_comapimerchantonboardcontactPhone', False)


    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}addressUpdatable uses Python identifier addressUpdatable
    __addressUpdatable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), 'addressUpdatable', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalUpdatable__httppsp_litle_comapimerchantonboardaddressUpdatable', False)


    addressUpdatable = property(__addressUpdatable.value, __addressUpdatable.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), 'emailAddress', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalUpdatable__httppsp_litle_comapimerchantonboardemailAddress', False)


    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)


    _ElementMap = {
        __contactPhone.name() : __contactPhone,
        __addressUpdatable.name() : __addressUpdatable,
        __emailAddress.name() : __emailAddress
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityPrincipalUpdatable', legalEntityPrincipalUpdatable_)


# Complex type businessResult with content type ELEMENT_ONLY
class businessResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}verificationResult uses Python identifier verificationResult
    __verificationResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verificationResult'), 'verificationResult', '__httppsp_litle_comapimerchantonboard_businessResult_httppsp_litle_comapimerchantonboardverificationResult', False)


    verificationResult = property(__verificationResult.value, __verificationResult.set, None, None)


    _ElementMap = {
        __verificationResult.name() : __verificationResult
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessResult', businessResult)


# Complex type subMerchantCreateRequest_ with content type ELEMENT_ONLY
class subMerchantCreateRequest_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantCreateRequest')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}createCredentials uses Python identifier createCredentials
    __createCredentials = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'createCredentials'), 'createCredentials', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardcreateCredentials', False)


    createCredentials = property(__createCredentials.value, __createCredentials.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankRoutingNumber uses Python identifier bankRoutingNumber
    __bankRoutingNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber'), 'bankRoutingNumber', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardbankRoutingNumber', False)


    bankRoutingNumber = property(__bankRoutingNumber.value, __bankRoutingNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}maxTransactionAmount uses Python identifier maxTransactionAmount
    __maxTransactionAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount'), 'maxTransactionAmount', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardmaxTransactionAmount', False)


    maxTransactionAmount = property(__maxTransactionAmount.value, __maxTransactionAmount.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}pspMerchantId uses Python identifier pspMerchantId
    __pspMerchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pspMerchantId'), 'pspMerchantId', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardpspMerchantId', False)


    pspMerchantId = property(__pspMerchantId.value, __pspMerchantId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}eCheckCompanyName uses Python identifier eCheckCompanyName
    __eCheckCompanyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName'), 'eCheckCompanyName', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardeCheckCompanyName', False)


    eCheckCompanyName = property(__eCheckCompanyName.value, __eCheckCompanyName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankAccountNumber uses Python identifier bankAccountNumber
    __bankAccountNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber'), 'bankAccountNumber', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardbankAccountNumber', False)


    bankAccountNumber = property(__bankAccountNumber.value, __bankAccountNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}url uses Python identifier url
    __url = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardurl', False)


    url = property(__url.value, __url.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}amexMid uses Python identifier amexMid
    __amexMid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexMid'), 'amexMid', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardamexMid', False)


    amexMid = property(__amexMid.value, __amexMid.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}purchaseCurrency uses Python identifier purchaseCurrency
    __purchaseCurrency = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'purchaseCurrency'), 'purchaseCurrency', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardpurchaseCurrency', False)


    purchaseCurrency = property(__purchaseCurrency.value, __purchaseCurrency.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'address'), 'address', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardaddress', False)


    address = property(__address.value, __address.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}customerServiceNumber uses Python identifier customerServiceNumber
    __customerServiceNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber'), 'customerServiceNumber', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardcustomerServiceNumber', False)


    customerServiceNumber = property(__customerServiceNumber.value, __customerServiceNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}eCheckBillingDescriptor uses Python identifier eCheckBillingDescriptor
    __eCheckBillingDescriptor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor'), 'eCheckBillingDescriptor', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardeCheckBillingDescriptor', False)


    eCheckBillingDescriptor = property(__eCheckBillingDescriptor.value, __eCheckBillingDescriptor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'primaryContact'), 'primaryContact', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardprimaryContact', False)


    primaryContact = property(__primaryContact.value, __primaryContact.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}hardCodedBillingDescriptor uses Python identifier hardCodedBillingDescriptor
    __hardCodedBillingDescriptor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor'), 'hardCodedBillingDescriptor', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardhardCodedBillingDescriptor', False)


    hardCodedBillingDescriptor = property(__hardCodedBillingDescriptor.value, __hardCodedBillingDescriptor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}discoverConveyedMid uses Python identifier discoverConveyedMid
    __discoverConveyedMid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid'), 'discoverConveyedMid', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboarddiscoverConveyedMid', False)


    discoverConveyedMid = property(__discoverConveyedMid.value, __discoverConveyedMid.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}merchantCategoryCode uses Python identifier merchantCategoryCode
    __merchantCategoryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantCategoryCode'), 'merchantCategoryCode', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardmerchantCategoryCode', False)


    merchantCategoryCode = property(__merchantCategoryCode.value, __merchantCategoryCode.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}merchantName uses Python identifier merchantName
    __merchantName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantName'), 'merchantName', '__httppsp_litle_comapimerchantonboard_subMerchantCreateRequest__httppsp_litle_comapimerchantonboardmerchantName', False)


    merchantName = property(__merchantName.value, __merchantName.set, None, None)


    _ElementMap = {
        __createCredentials.name() : __createCredentials,
        __bankRoutingNumber.name() : __bankRoutingNumber,
        __maxTransactionAmount.name() : __maxTransactionAmount,
        __pspMerchantId.name() : __pspMerchantId,
        __eCheckCompanyName.name() : __eCheckCompanyName,
        __bankAccountNumber.name() : __bankAccountNumber,
        __url.name() : __url,
        __amexMid.name() : __amexMid,
        __purchaseCurrency.name() : __purchaseCurrency,
        __address.name() : __address,
        __customerServiceNumber.name() : __customerServiceNumber,
        __eCheckBillingDescriptor.name() : __eCheckBillingDescriptor,
        __primaryContact.name() : __primaryContact,
        __hardCodedBillingDescriptor.name() : __hardCodedBillingDescriptor,
        __discoverConveyedMid.name() : __discoverConveyedMid,
        __merchantCategoryCode.name() : __merchantCategoryCode,
        __merchantName.name() : __merchantName
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'subMerchantCreateRequest', subMerchantCreateRequest_)


# Complex type subMerchantRetrievalResponse_ with content type ELEMENT_ONLY
class subMerchantRetrievalResponse_ (subMerchantCreateRequest_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantRetrievalResponse')
    # Base type is subMerchantCreateRequest_

    # Element createCredentials ({http://psp.litle.com/api/merchant/onboard}createCredentials) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element eCheckCompanyName ({http://psp.litle.com/api/merchant/onboard}eCheckCompanyName) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element eCheckBillingDescriptor ({http://psp.litle.com/api/merchant/onboard}eCheckBillingDescriptor) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element customerServiceNumber ({http://psp.litle.com/api/merchant/onboard}customerServiceNumber) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}updateDate uses Python identifier updateDate
    __updateDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), 'updateDate', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardupdateDate', False)


    updateDate = property(__updateDate.value, __updateDate.set, None, None)


    # Element hardCodedBillingDescriptor ({http://psp.litle.com/api/merchant/onboard}hardCodedBillingDescriptor) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element maxTransactionAmount ({http://psp.litle.com/api/merchant/onboard}maxTransactionAmount) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element purchaseCurrency ({http://psp.litle.com/api/merchant/onboard}purchaseCurrency) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}subMerchantId uses Python identifier subMerchantId
    __subMerchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId'), 'subMerchantId', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardsubMerchantId', False)


    subMerchantId = property(__subMerchantId.value, __subMerchantId.set, None, None)


    # Element merchantCategoryCode ({http://psp.litle.com/api/merchant/onboard}merchantCategoryCode) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}disabled uses Python identifier disabled
    __disabled = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'disabled'), 'disabled', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboarddisabled', False)


    disabled = property(__disabled.value, __disabled.set, None, None)


    # Element url ({http://psp.litle.com/api/merchant/onboard}url) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element bankRoutingNumber ({http://psp.litle.com/api/merchant/onboard}bankRoutingNumber) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}merchantIdentString uses Python identifier merchantIdentString
    __merchantIdentString = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString'), 'merchantIdentString', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardmerchantIdentString', False)


    merchantIdentString = property(__merchantIdentString.value, __merchantIdentString.set, None, None)


    # Element bankAccountNumber ({http://psp.litle.com/api/merchant/onboard}bankAccountNumber) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}credentials uses Python identifier credentials
    __credentials = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'credentials'), 'credentials', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardcredentials', False)


    credentials = property(__credentials.value, __credentials.set, None, None)


    # Element merchantName ({http://psp.litle.com/api/merchant/onboard}merchantName) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), 'transactionId', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardtransactionId', False)


    transactionId = property(__transactionId.value, __transactionId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}paypageCredentials uses Python identifier paypageCredentials
    __paypageCredentials = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials'), 'paypageCredentials', '__httppsp_litle_comapimerchantonboard_subMerchantRetrievalResponse__httppsp_litle_comapimerchantonboardpaypageCredentials', False)


    paypageCredentials = property(__paypageCredentials.value, __paypageCredentials.set, None, None)


    # Element primaryContact ({http://psp.litle.com/api/merchant/onboard}primaryContact) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element amexMid ({http://psp.litle.com/api/merchant/onboard}amexMid) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element address ({http://psp.litle.com/api/merchant/onboard}address) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element pspMerchantId ({http://psp.litle.com/api/merchant/onboard}pspMerchantId) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    # Element discoverConveyedMid ({http://psp.litle.com/api/merchant/onboard}discoverConveyedMid) inherited from {http://psp.litle.com/api/merchant/onboard}subMerchantCreateRequest

    _ElementMap = subMerchantCreateRequest_._ElementMap.copy()
    _ElementMap.update({
        __updateDate.name() : __updateDate,
        __subMerchantId.name() : __subMerchantId,
        __disabled.name() : __disabled,
        __merchantIdentString.name() : __merchantIdentString,
        __credentials.name() : __credentials,
        __transactionId.name() : __transactionId,
        __paypageCredentials.name() : __paypageCredentials
    })
    _AttributeMap = subMerchantCreateRequest_._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'subMerchantRetrievalResponse', subMerchantRetrievalResponse_)


# Complex type subMerchantUpdatable_ with content type ELEMENT_ONLY
class subMerchantUpdatable_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantUpdatable')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}bankRoutingNumber uses Python identifier bankRoutingNumber
    __bankRoutingNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber'), 'bankRoutingNumber', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardbankRoutingNumber', False)


    bankRoutingNumber = property(__bankRoutingNumber.value, __bankRoutingNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}discoverConveyedMid uses Python identifier discoverConveyedMid
    __discoverConveyedMid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid'), 'discoverConveyedMid', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboarddiscoverConveyedMid', False)


    discoverConveyedMid = property(__discoverConveyedMid.value, __discoverConveyedMid.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}primaryContact uses Python identifier primaryContact
    __primaryContact = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'primaryContact'), 'primaryContact', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardprimaryContact', False)


    primaryContact = property(__primaryContact.value, __primaryContact.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}disable uses Python identifier disable
    __disable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'disable'), 'disable', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboarddisable', False)


    disable = property(__disable.value, __disable.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}maxTransactionAmount uses Python identifier maxTransactionAmount
    __maxTransactionAmount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount'), 'maxTransactionAmount', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardmaxTransactionAmount', False)


    maxTransactionAmount = property(__maxTransactionAmount.value, __maxTransactionAmount.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}hardCodedBillingDescriptor uses Python identifier hardCodedBillingDescriptor
    __hardCodedBillingDescriptor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor'), 'hardCodedBillingDescriptor', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardhardCodedBillingDescriptor', False)


    hardCodedBillingDescriptor = property(__hardCodedBillingDescriptor.value, __hardCodedBillingDescriptor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankAccountNumber uses Python identifier bankAccountNumber
    __bankAccountNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber'), 'bankAccountNumber', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardbankAccountNumber', False)


    bankAccountNumber = property(__bankAccountNumber.value, __bankAccountNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}url uses Python identifier url
    __url = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardurl', False)


    url = property(__url.value, __url.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}amexMid uses Python identifier amexMid
    __amexMid = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'amexMid'), 'amexMid', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardamexMid', False)


    amexMid = property(__amexMid.value, __amexMid.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}addressUpdatable uses Python identifier addressUpdatable
    __addressUpdatable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), 'addressUpdatable', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardaddressUpdatable', False)


    addressUpdatable = property(__addressUpdatable.value, __addressUpdatable.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}customerServiceNumber uses Python identifier customerServiceNumber
    __customerServiceNumber = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber'), 'customerServiceNumber', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardcustomerServiceNumber', False)


    customerServiceNumber = property(__customerServiceNumber.value, __customerServiceNumber.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}eCheckBillingDescriptor uses Python identifier eCheckBillingDescriptor
    __eCheckBillingDescriptor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor'), 'eCheckBillingDescriptor', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardeCheckBillingDescriptor', False)


    eCheckBillingDescriptor = property(__eCheckBillingDescriptor.value, __eCheckBillingDescriptor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}eCheckCompanyName uses Python identifier eCheckCompanyName
    __eCheckCompanyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName'), 'eCheckCompanyName', '__httppsp_litle_comapimerchantonboard_subMerchantUpdatable__httppsp_litle_comapimerchantonboardeCheckCompanyName', False)


    eCheckCompanyName = property(__eCheckCompanyName.value, __eCheckCompanyName.set, None, None)


    _ElementMap = {
        __bankRoutingNumber.name() : __bankRoutingNumber,
        __discoverConveyedMid.name() : __discoverConveyedMid,
        __primaryContact.name() : __primaryContact,
        __disable.name() : __disable,
        __maxTransactionAmount.name() : __maxTransactionAmount,
        __hardCodedBillingDescriptor.name() : __hardCodedBillingDescriptor,
        __bankAccountNumber.name() : __bankAccountNumber,
        __url.name() : __url,
        __amexMid.name() : __amexMid,
        __addressUpdatable.name() : __addressUpdatable,
        __customerServiceNumber.name() : __customerServiceNumber,
        __eCheckBillingDescriptor.name() : __eCheckBillingDescriptor,
        __eCheckCompanyName.name() : __eCheckCompanyName
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'subMerchantUpdatable', subMerchantUpdatable_)


# Complex type principalResult with content type ELEMENT_ONLY
class principalResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}verificationResult uses Python identifier verificationResult
    __verificationResult = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verificationResult'), 'verificationResult', '__httppsp_litle_comapimerchantonboard_principalResult_httppsp_litle_comapimerchantonboardverificationResult', False)


    verificationResult = property(__verificationResult.value, __verificationResult.set, None, None)


    _ElementMap = {
        __verificationResult.name() : __verificationResult
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalResult', principalResult)


# Complex type bankruptcyResult with content type ELEMENT_ONLY
class bankruptcyResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'bankruptcyResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}zip4 uses Python identifier zip4
    __zip4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zip4'), 'zip4', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardzip4', False)


    zip4 = property(__zip4.value, __zip4.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankruptcyCount uses Python identifier bankruptcyCount
    __bankruptcyCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyCount'), 'bankruptcyCount', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardbankruptcyCount', False)


    bankruptcyCount = property(__bankruptcyCount.value, __bankruptcyCount.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}filingDate uses Python identifier filingDate
    __filingDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'filingDate'), 'filingDate', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardfilingDate', False)


    filingDate = property(__filingDate.value, __filingDate.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'companyName'), 'companyName', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardcompanyName', False)


    companyName = property(__companyName.value, __companyName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), 'streetAddress2', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardstreetAddress2', False)


    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardstate', False)


    state = property(__state.value, __state.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), 'streetAddress1', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardstreetAddress1', False)


    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardcity', False)


    city = property(__city.value, __city.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardzip', False)


    zip = property(__zip.value, __zip.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}bankruptcyType uses Python identifier bankruptcyType
    __bankruptcyType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyType'), 'bankruptcyType', '__httppsp_litle_comapimerchantonboard_bankruptcyResult_httppsp_litle_comapimerchantonboardbankruptcyType', False)


    bankruptcyType = property(__bankruptcyType.value, __bankruptcyType.set, None, None)


    _ElementMap = {
        __zip4.name() : __zip4,
        __bankruptcyCount.name() : __bankruptcyCount,
        __filingDate.name() : __filingDate,
        __companyName.name() : __companyName,
        __streetAddress2.name() : __streetAddress2,
        __state.name() : __state,
        __streetAddress1.name() : __streetAddress1,
        __city.name() : __city,
        __zip.name() : __zip,
        __bankruptcyType.name() : __bankruptcyType
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'bankruptcyResult', bankruptcyResult)


# Complex type businessVerificationIndicators with content type ELEMENT_ONLY
class businessVerificationIndicators (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessVerificationIndicators')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}addressVerified uses Python identifier addressVerified
    __addressVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressVerified'), 'addressVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardaddressVerified', False)


    addressVerified = property(__addressVerified.value, __addressVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}phoneVerified uses Python identifier phoneVerified
    __phoneVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified'), 'phoneVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardphoneVerified', False)


    phoneVerified = property(__phoneVerified.value, __phoneVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameVerified uses Python identifier nameVerified
    __nameVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameVerified'), 'nameVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardnameVerified', False)


    nameVerified = property(__nameVerified.value, __nameVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}cityVerified uses Python identifier cityVerified
    __cityVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cityVerified'), 'cityVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardcityVerified', False)


    cityVerified = property(__cityVerified.value, __cityVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}stateVerified uses Python identifier stateVerified
    __stateVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'stateVerified'), 'stateVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardstateVerified', False)


    stateVerified = property(__stateVerified.value, __stateVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}taxIdVerified uses Python identifier taxIdVerified
    __taxIdVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'taxIdVerified'), 'taxIdVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardtaxIdVerified', False)


    taxIdVerified = property(__taxIdVerified.value, __taxIdVerified.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}zipVerified uses Python identifier zipVerified
    __zipVerified = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zipVerified'), 'zipVerified', '__httppsp_litle_comapimerchantonboard_businessVerificationIndicators_httppsp_litle_comapimerchantonboardzipVerified', False)


    zipVerified = property(__zipVerified.value, __zipVerified.set, None, None)


    _ElementMap = {
        __addressVerified.name() : __addressVerified,
        __phoneVerified.name() : __phoneVerified,
        __nameVerified.name() : __nameVerified,
        __cityVerified.name() : __cityVerified,
        __stateVerified.name() : __stateVerified,
        __taxIdVerified.name() : __taxIdVerified,
        __zipVerified.name() : __zipVerified
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessVerificationIndicators', businessVerificationIndicators)


# Complex type legalEntityRetrievalResponse_ with content type ELEMENT_ONLY
class legalEntityRetrievalResponse_ (legalEntityCreateRequest_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityRetrievalResponse')
    # Base type is legalEntityCreateRequest_

    # Element taxId ({http://psp.litle.com/api/merchant/onboard}taxId) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}transactionId uses Python identifier transactionId
    __transactionId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), 'transactionId', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardtransactionId', False)


    transactionId = property(__transactionId.value, __transactionId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}responseCode uses Python identifier responseCode
    __responseCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), 'responseCode', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardresponseCode', False)


    responseCode = property(__responseCode.value, __responseCode.set, None, None)


    # Element hasAcceptedCreditCards ({http://psp.litle.com/api/merchant/onboard}hasAcceptedCreditCards) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}legalEntityId uses Python identifier legalEntityId
    __legalEntityId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId'), 'legalEntityId', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardlegalEntityId', False)


    legalEntityId = property(__legalEntityId.value, __legalEntityId.set, None, None)


    # Element legalEntityType ({http://psp.litle.com/api/merchant/onboard}legalEntityType) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element contactPhone ({http://psp.litle.com/api/merchant/onboard}contactPhone) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element PCI ({http://psp.litle.com/api/merchant/onboard}PCI) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element address ({http://psp.litle.com/api/merchant/onboard}address) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}decisionDate uses Python identifier decisionDate
    __decisionDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'decisionDate'), 'decisionDate', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboarddecisionDate', False)


    decisionDate = property(__decisionDate.value, __decisionDate.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}responseDescription uses Python identifier responseDescription
    __responseDescription = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'responseDescription'), 'responseDescription', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardresponseDescription', False)


    responseDescription = property(__responseDescription.value, __responseDescription.set, None, None)


    # Element legalEntityName ({http://psp.litle.com/api/merchant/onboard}legalEntityName) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element principals ({http://psp.litle.com/api/merchant/onboard}principals) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element annualCreditCardSalesVolume ({http://psp.litle.com/api/merchant/onboard}annualCreditCardSalesVolume) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    # Element {http://psp.litle.com/api/merchant/onboard}updateDate uses Python identifier updateDate
    __updateDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), 'updateDate', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardupdateDate', False)


    updateDate = property(__updateDate.value, __updateDate.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}backgroundCheckResults uses Python identifier backgroundCheckResults
    __backgroundCheckResults = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults'), 'backgroundCheckResults', '__httppsp_litle_comapimerchantonboard_legalEntityRetrievalResponse__httppsp_litle_comapimerchantonboardbackgroundCheckResults', False)


    backgroundCheckResults = property(__backgroundCheckResults.value, __backgroundCheckResults.set, None, None)


    # Element doingBusinessAs ({http://psp.litle.com/api/merchant/onboard}doingBusinessAs) inherited from {http://psp.litle.com/api/merchant/onboard}legalEntityCreateRequest

    _ElementMap = legalEntityCreateRequest_._ElementMap.copy()
    _ElementMap.update({
        __transactionId.name() : __transactionId,
        __responseCode.name() : __responseCode,
        __legalEntityId.name() : __legalEntityId,
        __decisionDate.name() : __decisionDate,
        __responseDescription.name() : __responseDescription,
        __updateDate.name() : __updateDate,
        __backgroundCheckResults.name() : __backgroundCheckResults
    })
    _AttributeMap = legalEntityCreateRequest_._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'legalEntityRetrievalResponse', legalEntityRetrievalResponse_)


# Complex type lienResult with content type ELEMENT_ONLY
class lienResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lienResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}releasedCount uses Python identifier releasedCount
    __releasedCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'releasedCount'), 'releasedCount', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardreleasedCount', False)


    releasedCount = property(__releasedCount.value, __releasedCount.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}unreleasedCount uses Python identifier unreleasedCount
    __unreleasedCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'unreleasedCount'), 'unreleasedCount', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardunreleasedCount', False)


    unreleasedCount = property(__unreleasedCount.value, __unreleasedCount.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}filingDate uses Python identifier filingDate
    __filingDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'filingDate'), 'filingDate', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardfilingDate', False)


    filingDate = property(__filingDate.value, __filingDate.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}companyName uses Python identifier companyName
    __companyName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'companyName'), 'companyName', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardcompanyName', False)


    companyName = property(__companyName.value, __companyName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardcity', False)


    city = property(__city.value, __city.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), 'streetAddress2', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardstreetAddress2', False)


    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}state uses Python identifier state
    __state = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'state'), 'state', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardstate', False)


    state = property(__state.value, __state.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}lienType uses Python identifier lienType
    __lienType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lienType'), 'lienType', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardlienType', False)


    lienType = property(__lienType.value, __lienType.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zip'), 'zip', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardzip', False)


    zip = property(__zip.value, __zip.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), 'streetAddress1', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardstreetAddress1', False)


    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}zip4 uses Python identifier zip4
    __zip4 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'zip4'), 'zip4', '__httppsp_litle_comapimerchantonboard_lienResult_httppsp_litle_comapimerchantonboardzip4', False)


    zip4 = property(__zip4.value, __zip4.set, None, None)


    _ElementMap = {
        __releasedCount.name() : __releasedCount,
        __unreleasedCount.name() : __unreleasedCount,
        __filingDate.name() : __filingDate,
        __companyName.name() : __companyName,
        __city.name() : __city,
        __streetAddress2.name() : __streetAddress2,
        __state.name() : __state,
        __lienType.name() : __lienType,
        __zip.name() : __zip,
        __streetAddress1.name() : __streetAddress1,
        __zip4.name() : __zip4
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'lienResult', lienResult)


# Complex type CTD_ANON_2 with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}riskIndicator uses Python identifier riskIndicator
    __riskIndicator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator'), 'riskIndicator', '__httppsp_litle_comapimerchantonboard_CTD_ANON_2_httppsp_litle_comapimerchantonboardriskIndicator', True)


    riskIndicator = property(__riskIndicator.value, __riskIndicator.set, None, None)


    _ElementMap = {
        __riskIndicator.name() : __riskIndicator
    }
    _AttributeMap = {

    }



# Complex type businessVerificationResult with content type ELEMENT_ONLY
class businessVerificationResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessVerificationResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}riskIndicators uses Python identifier riskIndicators
    __riskIndicators = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators'), 'riskIndicators', '__httppsp_litle_comapimerchantonboard_businessVerificationResult_httppsp_litle_comapimerchantonboardriskIndicators', False)


    riskIndicators = property(__riskIndicators.value, __riskIndicators.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameAddressPhoneAssociation uses Python identifier nameAddressPhoneAssociation
    __nameAddressPhoneAssociation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation'), 'nameAddressPhoneAssociation', '__httppsp_litle_comapimerchantonboard_businessVerificationResult_httppsp_litle_comapimerchantonboardnameAddressPhoneAssociation', False)


    nameAddressPhoneAssociation = property(__nameAddressPhoneAssociation.value, __nameAddressPhoneAssociation.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}verificationIndicators uses Python identifier verificationIndicators
    __verificationIndicators = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators'), 'verificationIndicators', '__httppsp_litle_comapimerchantonboard_businessVerificationResult_httppsp_litle_comapimerchantonboardverificationIndicators', False)


    verificationIndicators = property(__verificationIndicators.value, __verificationIndicators.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameAddressTaxIdAssociation uses Python identifier nameAddressTaxIdAssociation
    __nameAddressTaxIdAssociation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameAddressTaxIdAssociation'), 'nameAddressTaxIdAssociation', '__httppsp_litle_comapimerchantonboard_businessVerificationResult_httppsp_litle_comapimerchantonboardnameAddressTaxIdAssociation', False)


    nameAddressTaxIdAssociation = property(__nameAddressTaxIdAssociation.value, __nameAddressTaxIdAssociation.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}overallScore uses Python identifier overallScore
    __overallScore = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'overallScore'), 'overallScore', '__httppsp_litle_comapimerchantonboard_businessVerificationResult_httppsp_litle_comapimerchantonboardoverallScore', False)


    overallScore = property(__overallScore.value, __overallScore.set, None, None)


    _ElementMap = {
        __riskIndicators.name() : __riskIndicators,
        __nameAddressPhoneAssociation.name() : __nameAddressPhoneAssociation,
        __verificationIndicators.name() : __verificationIndicators,
        __nameAddressTaxIdAssociation.name() : __nameAddressTaxIdAssociation,
        __overallScore.name() : __overallScore
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessVerificationResult', businessVerificationResult)


# Complex type paypageCredential with content type ELEMENT_ONLY
class paypageCredential (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'paypageCredential')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}paypageId uses Python identifier paypageId
    __paypageId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageId'), 'paypageId', '__httppsp_litle_comapimerchantonboard_paypageCredential_httppsp_litle_comapimerchantonboardpaypageId', False)


    paypageId = property(__paypageId.value, __paypageId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}username uses Python identifier username
    __username = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'username'), 'username', '__httppsp_litle_comapimerchantonboard_paypageCredential_httppsp_litle_comapimerchantonboardusername', False)


    username = property(__username.value, __username.set, None, None)


    _ElementMap = {
        __paypageId.name() : __paypageId,
        __username.name() : __username
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'paypageCredential', paypageCredential)


# Complex type principalVerificationResult with content type ELEMENT_ONLY
class principalVerificationResult (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalVerificationResult')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}riskIndicators uses Python identifier riskIndicators
    __riskIndicators = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators'), 'riskIndicators', '__httppsp_litle_comapimerchantonboard_principalVerificationResult_httppsp_litle_comapimerchantonboardriskIndicators', False)


    riskIndicators = property(__riskIndicators.value, __riskIndicators.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameAddressPhoneAssociation uses Python identifier nameAddressPhoneAssociation
    __nameAddressPhoneAssociation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation'), 'nameAddressPhoneAssociation', '__httppsp_litle_comapimerchantonboard_principalVerificationResult_httppsp_litle_comapimerchantonboardnameAddressPhoneAssociation', False)


    nameAddressPhoneAssociation = property(__nameAddressPhoneAssociation.value, __nameAddressPhoneAssociation.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}verificationIndicators uses Python identifier verificationIndicators
    __verificationIndicators = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators'), 'verificationIndicators', '__httppsp_litle_comapimerchantonboard_principalVerificationResult_httppsp_litle_comapimerchantonboardverificationIndicators', False)


    verificationIndicators = property(__verificationIndicators.value, __verificationIndicators.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}overallScore uses Python identifier overallScore
    __overallScore = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'overallScore'), 'overallScore', '__httppsp_litle_comapimerchantonboard_principalVerificationResult_httppsp_litle_comapimerchantonboardoverallScore', False)


    overallScore = property(__overallScore.value, __overallScore.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}nameAddressSsnAssociation uses Python identifier nameAddressSsnAssociation
    __nameAddressSsnAssociation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nameAddressSsnAssociation'), 'nameAddressSsnAssociation', '__httppsp_litle_comapimerchantonboard_principalVerificationResult_httppsp_litle_comapimerchantonboardnameAddressSsnAssociation', False)


    nameAddressSsnAssociation = property(__nameAddressSsnAssociation.value, __nameAddressSsnAssociation.set, None, None)


    _ElementMap = {
        __riskIndicators.name() : __riskIndicators,
        __nameAddressPhoneAssociation.name() : __nameAddressPhoneAssociation,
        __verificationIndicators.name() : __verificationIndicators,
        __overallScore.name() : __overallScore,
        __nameAddressSsnAssociation.name() : __nameAddressSsnAssociation
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalVerificationResult', principalVerificationResult)


# Complex type legalEntityPrincipalCreateResponse with content type ELEMENT_ONLY
class legalEntityPrincipalCreateResponse (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityPrincipalCreateResponse')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalCreateResponse_httppsp_litle_comapimerchantonboardlastName', False)


    lastName = property(__lastName.value, __lastName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principalId'), 'principalId', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalCreateResponse_httppsp_litle_comapimerchantonboardprincipalId', False)


    principalId = property(__principalId.value, __principalId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipalCreateResponse_httppsp_litle_comapimerchantonboardfirstName', False)


    firstName = property(__firstName.value, __firstName.set, None, None)


    _ElementMap = {
        __lastName.name() : __lastName,
        __principalId.name() : __principalId,
        __firstName.name() : __firstName
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityPrincipalCreateResponse', legalEntityPrincipalCreateResponse)


# Complex type addressUpdatable with content type ELEMENT_ONLY
class addressUpdatable (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress2 uses Python identifier streetAddress2
    __streetAddress2 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), 'streetAddress2', '__httppsp_litle_comapimerchantonboard_addressUpdatable_httppsp_litle_comapimerchantonboardstreetAddress2', False)


    streetAddress2 = property(__streetAddress2.value, __streetAddress2.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'stateProvince'), 'stateProvince', '__httppsp_litle_comapimerchantonboard_addressUpdatable_httppsp_litle_comapimerchantonboardstateProvince', False)


    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}city uses Python identifier city
    __city = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httppsp_litle_comapimerchantonboard_addressUpdatable_httppsp_litle_comapimerchantonboardcity', False)


    city = property(__city.value, __city.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}streetAddress1 uses Python identifier streetAddress1
    __streetAddress1 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), 'streetAddress1', '__httppsp_litle_comapimerchantonboard_addressUpdatable_httppsp_litle_comapimerchantonboardstreetAddress1', False)


    streetAddress1 = property(__streetAddress1.value, __streetAddress1.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}postalCode uses Python identifier postalCode
    __postalCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), 'postalCode', '__httppsp_litle_comapimerchantonboard_addressUpdatable_httppsp_litle_comapimerchantonboardpostalCode', False)


    postalCode = property(__postalCode.value, __postalCode.set, None, None)


    _ElementMap = {
        __streetAddress2.name() : __streetAddress2,
        __stateProvince.name() : __stateProvince,
        __city.name() : __city,
        __streetAddress1.name() : __streetAddress1,
        __postalCode.name() : __postalCode
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'addressUpdatable', addressUpdatable)


# Complex type address with content type ELEMENT_ONLY
class address (addressUpdatable):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'address')
    # Base type is addressUpdatable

    # Element streetAddress1 ({http://psp.litle.com/api/merchant/onboard}streetAddress1) inherited from {http://psp.litle.com/api/merchant/onboard}addressUpdatable

    # Element stateProvince ({http://psp.litle.com/api/merchant/onboard}stateProvince) inherited from {http://psp.litle.com/api/merchant/onboard}addressUpdatable

    # Element {http://psp.litle.com/api/merchant/onboard}countryCode uses Python identifier countryCode
    __countryCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'countryCode'), 'countryCode', '__httppsp_litle_comapimerchantonboard_address_httppsp_litle_comapimerchantonboardcountryCode', False)


    countryCode = property(__countryCode.value, __countryCode.set, None, None)


    # Element streetAddress2 ({http://psp.litle.com/api/merchant/onboard}streetAddress2) inherited from {http://psp.litle.com/api/merchant/onboard}addressUpdatable

    # Element postalCode ({http://psp.litle.com/api/merchant/onboard}postalCode) inherited from {http://psp.litle.com/api/merchant/onboard}addressUpdatable

    # Element city ({http://psp.litle.com/api/merchant/onboard}city) inherited from {http://psp.litle.com/api/merchant/onboard}addressUpdatable

    _ElementMap = addressUpdatable._ElementMap.copy()
    _ElementMap.update({
        __countryCode.name() : __countryCode
    })
    _AttributeMap = addressUpdatable._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'address', address)


# Complex type subMerchantCreateResponse_ with content type ELEMENT_ONLY
class subMerchantCreateResponse_ (response_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantCreateResponse')
    # Base type is response_

    # Element {http://psp.litle.com/api/merchant/onboard}credentials uses Python identifier credentials
    __credentials = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'credentials'), 'credentials', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__httppsp_litle_comapimerchantonboardcredentials', False)


    credentials = property(__credentials.value, __credentials.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}originalSubMerchant uses Python identifier originalSubMerchant
    __originalSubMerchant = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'originalSubMerchant'), 'originalSubMerchant', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__httppsp_litle_comapimerchantonboardoriginalSubMerchant', False)


    originalSubMerchant = property(__originalSubMerchant.value, __originalSubMerchant.set, None, None)


    # Element transactionId ({http://psp.litle.com/api/merchant/onboard}transactionId) inherited from {http://psp.litle.com/api/merchant/onboard}response

    # Element {http://psp.litle.com/api/merchant/onboard}subMerchantId uses Python identifier subMerchantId
    __subMerchantId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId'), 'subMerchantId', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__httppsp_litle_comapimerchantonboardsubMerchantId', False)


    subMerchantId = property(__subMerchantId.value, __subMerchantId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}paypageCredentials uses Python identifier paypageCredentials
    __paypageCredentials = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials'), 'paypageCredentials', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__httppsp_litle_comapimerchantonboardpaypageCredentials', False)


    paypageCredentials = property(__paypageCredentials.value, __paypageCredentials.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}merchantIdentString uses Python identifier merchantIdentString
    __merchantIdentString = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString'), 'merchantIdentString', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__httppsp_litle_comapimerchantonboardmerchantIdentString', False)


    merchantIdentString = property(__merchantIdentString.value, __merchantIdentString.set, None, None)


    # Attribute duplicate uses Python identifier duplicate
    __duplicate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'duplicate'), 'duplicate', '__httppsp_litle_comapimerchantonboard_subMerchantCreateResponse__duplicate', pyxb.binding.datatypes.boolean)

    duplicate = property(__duplicate.value, __duplicate.set, None, None)


    _ElementMap = response_._ElementMap.copy()
    _ElementMap.update({
        __credentials.name() : __credentials,
        __originalSubMerchant.name() : __originalSubMerchant,
        __subMerchantId.name() : __subMerchantId,
        __paypageCredentials.name() : __paypageCredentials,
        __merchantIdentString.name() : __merchantIdentString
    })
    _AttributeMap = response_._AttributeMap.copy()
    _AttributeMap.update({
        __duplicate.name() : __duplicate
    })
Namespace.addCategoryObject('typeBinding', u'subMerchantCreateResponse', subMerchantCreateResponse_)


# Complex type legalEntityPciInfo with content type ELEMENT_ONLY
class legalEntityPciInfo (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityPciInfo')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}pciLevel uses Python identifier pciLevel
    __pciLevel = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pciLevel'), 'pciLevel', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardpciLevel', False)


    pciLevel = property(__pciLevel.value, __pciLevel.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}qualifiedSecurityAssessor uses Python identifier qualifiedSecurityAssessor
    __qualifiedSecurityAssessor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'qualifiedSecurityAssessor'), 'qualifiedSecurityAssessor', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardqualifiedSecurityAssessor', False)


    qualifiedSecurityAssessor = property(__qualifiedSecurityAssessor.value, __qualifiedSecurityAssessor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}isExclusiveToPsp uses Python identifier isExclusiveToPsp
    __isExclusiveToPsp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'isExclusiveToPsp'), 'isExclusiveToPsp', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardisExclusiveToPsp', False)


    isExclusiveToPsp = property(__isExclusiveToPsp.value, __isExclusiveToPsp.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}reportOnCompliance uses Python identifier reportOnCompliance
    __reportOnCompliance = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'reportOnCompliance'), 'reportOnCompliance', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardreportOnCompliance', False)


    reportOnCompliance = property(__reportOnCompliance.value, __reportOnCompliance.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}mostRecentlyPassedScan uses Python identifier mostRecentlyPassedScan
    __mostRecentlyPassedScan = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'mostRecentlyPassedScan'), 'mostRecentlyPassedScan', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardmostRecentlyPassedScan', False)


    mostRecentlyPassedScan = property(__mostRecentlyPassedScan.value, __mostRecentlyPassedScan.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}scanningVendor uses Python identifier scanningVendor
    __scanningVendor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scanningVendor'), 'scanningVendor', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardscanningVendor', False)


    scanningVendor = property(__scanningVendor.value, __scanningVendor.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}isPciComplianceValidated uses Python identifier isPciComplianceValidated
    __isPciComplianceValidated = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'isPciComplianceValidated'), 'isPciComplianceValidated', '__httppsp_litle_comapimerchantonboard_legalEntityPciInfo_httppsp_litle_comapimerchantonboardisPciComplianceValidated', False)


    isPciComplianceValidated = property(__isPciComplianceValidated.value, __isPciComplianceValidated.set, None, None)


    _ElementMap = {
        __pciLevel.name() : __pciLevel,
        __qualifiedSecurityAssessor.name() : __qualifiedSecurityAssessor,
        __isExclusiveToPsp.name() : __isExclusiveToPsp,
        __reportOnCompliance.name() : __reportOnCompliance,
        __mostRecentlyPassedScan.name() : __mostRecentlyPassedScan,
        __scanningVendor.name() : __scanningVendor,
        __isPciComplianceValidated.name() : __isPciComplianceValidated
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityPciInfo', legalEntityPciInfo)


# Complex type nameAddressSsnAssociation with content type ELEMENT_ONLY
class nameAddressSsnAssociation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameAddressSsnAssociation')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_nameAddressSsnAssociation_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httppsp_litle_comapimerchantonboard_nameAddressSsnAssociation_httppsp_litle_comapimerchantonboardcode', False)


    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __code.name() : __code
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'nameAddressSsnAssociation', nameAddressSsnAssociation)


# Complex type principalNameAddressPhoneAssociation with content type ELEMENT_ONLY
class principalNameAddressPhoneAssociation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalNameAddressPhoneAssociation')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_principalNameAddressPhoneAssociation_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httppsp_litle_comapimerchantonboard_principalNameAddressPhoneAssociation_httppsp_litle_comapimerchantonboardcode', False)


    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __code.name() : __code
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalNameAddressPhoneAssociation', principalNameAddressPhoneAssociation)


# Complex type legalEntityPrincipal with content type ELEMENT_ONLY
class legalEntityPrincipal (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityPrincipal')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), 'dateOfBirth', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboarddateOfBirth', False)


    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardfirstName', False)


    firstName = property(__firstName.value, __firstName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}ssn uses Python identifier ssn
    __ssn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ssn'), 'ssn', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardssn', False)


    ssn = property(__ssn.value, __ssn.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}driversLicense uses Python identifier driversLicense
    __driversLicense = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'driversLicense'), 'driversLicense', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboarddriversLicense', False)


    driversLicense = property(__driversLicense.value, __driversLicense.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardlastName', False)


    lastName = property(__lastName.value, __lastName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}driversLicenseState uses Python identifier driversLicenseState
    __driversLicenseState = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'driversLicenseState'), 'driversLicenseState', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboarddriversLicenseState', False)


    driversLicenseState = property(__driversLicenseState.value, __driversLicenseState.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), 'contactPhone', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardcontactPhone', False)


    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}principalId uses Python identifier principalId
    __principalId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principalId'), 'principalId', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardprincipalId', False)


    principalId = property(__principalId.value, __principalId.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), 'emailAddress', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardemailAddress', False)


    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}address uses Python identifier address
    __address = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'address'), 'address', '__httppsp_litle_comapimerchantonboard_legalEntityPrincipal_httppsp_litle_comapimerchantonboardaddress', False)


    address = property(__address.value, __address.set, None, None)


    _ElementMap = {
        __dateOfBirth.name() : __dateOfBirth,
        __firstName.name() : __firstName,
        __ssn.name() : __ssn,
        __driversLicense.name() : __driversLicense,
        __lastName.name() : __lastName,
        __driversLicenseState.name() : __driversLicenseState,
        __contactPhone.name() : __contactPhone,
        __principalId.name() : __principalId,
        __emailAddress.name() : __emailAddress,
        __address.name() : __address
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityPrincipal', legalEntityPrincipal)


# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principal'), 'principal', '__httppsp_litle_comapimerchantonboard_CTD_ANON_3_httppsp_litle_comapimerchantonboardprincipal', False)


    principal = property(__principal.value, __principal.set, None, None)


    _ElementMap = {
        __principal.name() : __principal
    }
    _AttributeMap = {

    }



# Complex type legalEntityUpdatable_ with content type ELEMENT_ONLY
class legalEntityUpdatable_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'legalEntityUpdatable')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}addressUpdatable uses Python identifier addressUpdatable
    __addressUpdatable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), 'addressUpdatable', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboardaddressUpdatable', False)


    addressUpdatable = property(__addressUpdatable.value, __addressUpdatable.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}contactPhone uses Python identifier contactPhone
    __contactPhone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), 'contactPhone', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboardcontactPhone', False)


    contactPhone = property(__contactPhone.value, __contactPhone.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}annualCreditCardSalesVolume uses Python identifier annualCreditCardSalesVolume
    __annualCreditCardSalesVolume = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume'), 'annualCreditCardSalesVolume', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboardannualCreditCardSalesVolume', False)


    annualCreditCardSalesVolume = property(__annualCreditCardSalesVolume.value, __annualCreditCardSalesVolume.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}hasAcceptedCreditCards uses Python identifier hasAcceptedCreditCards
    __hasAcceptedCreditCards = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards'), 'hasAcceptedCreditCards', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboardhasAcceptedCreditCards', False)


    hasAcceptedCreditCards = property(__hasAcceptedCreditCards.value, __hasAcceptedCreditCards.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}PCI uses Python identifier PCI
    __PCI = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PCI'), 'PCI', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboardPCI', False)


    PCI = property(__PCI.value, __PCI.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}doingBusinessAs uses Python identifier doingBusinessAs
    __doingBusinessAs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs'), 'doingBusinessAs', '__httppsp_litle_comapimerchantonboard_legalEntityUpdatable__httppsp_litle_comapimerchantonboarddoingBusinessAs', False)


    doingBusinessAs = property(__doingBusinessAs.value, __doingBusinessAs.set, None, None)


    _ElementMap = {
        __addressUpdatable.name() : __addressUpdatable,
        __contactPhone.name() : __contactPhone,
        __annualCreditCardSalesVolume.name() : __annualCreditCardSalesVolume,
        __hasAcceptedCreditCards.name() : __hasAcceptedCreditCards,
        __PCI.name() : __PCI,
        __doingBusinessAs.name() : __doingBusinessAs
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'legalEntityUpdatable', legalEntityUpdatable_)


# Complex type approvedMccResponse_ with content type ELEMENT_ONLY
class approvedMccResponse_ (response_):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'approvedMccResponse')
    # Base type is response_

    # Element {http://psp.litle.com/api/merchant/onboard}approvedMccs uses Python identifier approvedMccs
    __approvedMccs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedMccs'), 'approvedMccs', '__httppsp_litle_comapimerchantonboard_approvedMccResponse__httppsp_litle_comapimerchantonboardapprovedMccs', False)


    approvedMccs = property(__approvedMccs.value, __approvedMccs.set, None, None)


    # Element transactionId ({http://psp.litle.com/api/merchant/onboard}transactionId) inherited from {http://psp.litle.com/api/merchant/onboard}response

    _ElementMap = response_._ElementMap.copy()
    _ElementMap.update({
        __approvedMccs.name() : __approvedMccs
    })
    _AttributeMap = response_._AttributeMap.copy()
    _AttributeMap.update({

    })
Namespace.addCategoryObject('typeBinding', u'approvedMccResponse', approvedMccResponse_)


# Complex type nameAddressTaxIdAssociation with content type ELEMENT_ONLY
class nameAddressTaxIdAssociation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameAddressTaxIdAssociation')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_nameAddressTaxIdAssociation_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httppsp_litle_comapimerchantonboard_nameAddressTaxIdAssociation_httppsp_litle_comapimerchantonboardcode', False)


    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __code.name() : __code
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'nameAddressTaxIdAssociation', nameAddressTaxIdAssociation)


# Complex type subMerchantCredentials with content type ELEMENT_ONLY
class subMerchantCredentials (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantCredentials')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}passwordExpirationDate uses Python identifier passwordExpirationDate
    __passwordExpirationDate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'passwordExpirationDate'), 'passwordExpirationDate', '__httppsp_litle_comapimerchantonboard_subMerchantCredentials_httppsp_litle_comapimerchantonboardpasswordExpirationDate', False)


    passwordExpirationDate = property(__passwordExpirationDate.value, __passwordExpirationDate.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}username uses Python identifier username
    __username = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'username'), 'username', '__httppsp_litle_comapimerchantonboard_subMerchantCredentials_httppsp_litle_comapimerchantonboardusername', False)


    username = property(__username.value, __username.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}password uses Python identifier password
    __password = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'password'), 'password', '__httppsp_litle_comapimerchantonboard_subMerchantCredentials_httppsp_litle_comapimerchantonboardpassword', False)


    password = property(__password.value, __password.set, None, None)


    _ElementMap = {
        __passwordExpirationDate.name() : __passwordExpirationDate,
        __username.name() : __username,
        __password.name() : __password
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'subMerchantCredentials', subMerchantCredentials)


# Complex type businessNameAddressPhoneAssociation with content type ELEMENT_ONLY
class businessNameAddressPhoneAssociation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessNameAddressPhoneAssociation')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_businessNameAddressPhoneAssociation_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}code uses Python identifier code
    __code = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httppsp_litle_comapimerchantonboard_businessNameAddressPhoneAssociation_httppsp_litle_comapimerchantonboardcode', False)


    code = property(__code.value, __code.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __code.name() : __code
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessNameAddressPhoneAssociation', businessNameAddressPhoneAssociation)


# Complex type subMerchantPrimaryContact with content type ELEMENT_ONLY
class subMerchantPrimaryContact (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subMerchantPrimaryContact')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httppsp_litle_comapimerchantonboard_subMerchantPrimaryContact_httppsp_litle_comapimerchantonboardfirstName', False)


    firstName = property(__firstName.value, __firstName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}emailAddress uses Python identifier emailAddress
    __emailAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), 'emailAddress', '__httppsp_litle_comapimerchantonboard_subMerchantPrimaryContact_httppsp_litle_comapimerchantonboardemailAddress', False)


    emailAddress = property(__emailAddress.value, __emailAddress.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httppsp_litle_comapimerchantonboard_subMerchantPrimaryContact_httppsp_litle_comapimerchantonboardlastName', False)


    lastName = property(__lastName.value, __lastName.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httppsp_litle_comapimerchantonboard_subMerchantPrimaryContact_httppsp_litle_comapimerchantonboardphone', False)


    phone = property(__phone.value, __phone.set, None, None)


    _ElementMap = {
        __firstName.name() : __firstName,
        __emailAddress.name() : __emailAddress,
        __lastName.name() : __lastName,
        __phone.name() : __phone
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'subMerchantPrimaryContact', subMerchantPrimaryContact)


# Complex type principalScore with content type ELEMENT_ONLY
class principalScore (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'principalScore')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_principalScore_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httppsp_litle_comapimerchantonboard_principalScore_httppsp_litle_comapimerchantonboardscore', False)


    score = property(__score.value, __score.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __score.name() : __score
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'principalScore', principalScore)


# Complex type businessToPrincipalAssociation with content type ELEMENT_ONLY
class businessToPrincipalAssociation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessToPrincipalAssociation')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_businessToPrincipalAssociation_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httppsp_litle_comapimerchantonboard_businessToPrincipalAssociation_httppsp_litle_comapimerchantonboardscore', False)


    score = property(__score.value, __score.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __score.name() : __score
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessToPrincipalAssociation', businessToPrincipalAssociation)


# Complex type CTD_ANON_4 with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}approvedMcc uses Python identifier approvedMcc
    __approvedMcc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'approvedMcc'), 'approvedMcc', '__httppsp_litle_comapimerchantonboard_CTD_ANON_4_httppsp_litle_comapimerchantonboardapprovedMcc', True)


    approvedMcc = property(__approvedMcc.value, __approvedMcc.set, None, None)


    _ElementMap = {
        __approvedMcc.name() : __approvedMcc
    }
    _AttributeMap = {

    }



# Complex type CTD_ANON_5 with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}principal uses Python identifier principal
    __principal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'principal'), 'principal', '__httppsp_litle_comapimerchantonboard_CTD_ANON_5_httppsp_litle_comapimerchantonboardprincipal', True)


    principal = property(__principal.value, __principal.set, None, None)


    _ElementMap = {
        __principal.name() : __principal
    }
    _AttributeMap = {

    }



# Complex type CTD_ANON_6 with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}error uses Python identifier error
    __error = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'error'), 'error', '__httppsp_litle_comapimerchantonboard_CTD_ANON_6_httppsp_litle_comapimerchantonboarderror', True)


    error = property(__error.value, __error.set, None, None)


    _ElementMap = {
        __error.name() : __error
    }
    _AttributeMap = {

    }



# Complex type CTD_ANON_7 with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}riskIndicator uses Python identifier riskIndicator
    __riskIndicator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator'), 'riskIndicator', '__httppsp_litle_comapimerchantonboard_CTD_ANON_7_httppsp_litle_comapimerchantonboardriskIndicator', True)


    riskIndicator = property(__riskIndicator.value, __riskIndicator.set, None, None)


    _ElementMap = {
        __riskIndicator.name() : __riskIndicator
    }
    _AttributeMap = {

    }



# Complex type businessScore with content type ELEMENT_ONLY
class businessScore (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'businessScore')
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://psp.litle.com/api/merchant/onboard}description uses Python identifier description
    __description = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httppsp_litle_comapimerchantonboard_businessScore_httppsp_litle_comapimerchantonboarddescription', False)


    description = property(__description.value, __description.set, None, None)


    # Element {http://psp.litle.com/api/merchant/onboard}score uses Python identifier score
    __score = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'score'), 'score', '__httppsp_litle_comapimerchantonboard_businessScore_httppsp_litle_comapimerchantonboardscore', False)


    score = property(__score.value, __score.set, None, None)


    _ElementMap = {
        __description.name() : __description,
        __score.name() : __score
    }
    _AttributeMap = {

    }
Namespace.addCategoryObject('typeBinding', u'businessScore', businessScore)


errorResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errorResponse'), errorResponse_)
Namespace.addCategoryObject('elementBinding', errorResponse.name().localName(), errorResponse)

backgroundCheckResults = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults'), backgroundCheckResults_)
Namespace.addCategoryObject('elementBinding', backgroundCheckResults.name().localName(), backgroundCheckResults)

legalEntityCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityCreateRequest'), legalEntityCreateRequest_)
Namespace.addCategoryObject('elementBinding', legalEntityCreateRequest.name().localName(), legalEntityCreateRequest)

legalEntityCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityCreateResponse'), legalEntityCreateResponse_)
Namespace.addCategoryObject('elementBinding', legalEntityCreateResponse.name().localName(), legalEntityCreateResponse)

legalEntityPrincipalUpdatable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityPrincipalUpdatable'), legalEntityPrincipalUpdatable_)
Namespace.addCategoryObject('elementBinding', legalEntityPrincipalUpdatable.name().localName(), legalEntityPrincipalUpdatable)

subMerchantCreateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantCreateRequest'), subMerchantCreateRequest_)
Namespace.addCategoryObject('elementBinding', subMerchantCreateRequest.name().localName(), subMerchantCreateRequest)

subMerchantRetrievalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantRetrievalResponse'), subMerchantRetrievalResponse_)
Namespace.addCategoryObject('elementBinding', subMerchantRetrievalResponse.name().localName(), subMerchantRetrievalResponse)

subMerchantUpdatable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantUpdatable'), subMerchantUpdatable_)
Namespace.addCategoryObject('elementBinding', subMerchantUpdatable.name().localName(), subMerchantUpdatable)

legalEntityRetrievalResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityRetrievalResponse'), legalEntityRetrievalResponse_)
Namespace.addCategoryObject('elementBinding', legalEntityRetrievalResponse.name().localName(), legalEntityRetrievalResponse)

subMerchantCreateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantCreateResponse'), subMerchantCreateResponse_)
Namespace.addCategoryObject('elementBinding', subMerchantCreateResponse.name().localName(), subMerchantCreateResponse)

legalEntityUpdatable = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityUpdatable'), legalEntityUpdatable_)
Namespace.addCategoryObject('elementBinding', legalEntityUpdatable.name().localName(), legalEntityUpdatable)

approvedMccResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedMccResponse'), approvedMccResponse_)
Namespace.addCategoryObject('elementBinding', approvedMccResponse.name().localName(), approvedMccResponse)

response = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'response'), response_)
Namespace.addCategoryObject('elementBinding', response.name().localName(), response)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential'), paypageCredential, scope=CTD_ANON))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



principalAddressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_31, scope=principalAddressUpdatable))

principalAddressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), STD_ANON_24, scope=principalAddressUpdatable))

principalAddressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stateProvince'), STD_ANON_41, scope=principalAddressUpdatable))

principalAddressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), STD_ANON_9, scope=principalAddressUpdatable))

principalAddressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), STD_ANON_12, scope=principalAddressUpdatable))
principalAddressUpdatable._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalAddressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stateProvince')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), min_occurs=1, max_occurs=1)
    )
principalAddressUpdatable._ContentModel = pyxb.binding.content.ParticleModel(principalAddressUpdatable._GroupModel, min_occurs=1, max_occurs=1)



response_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), pyxb.binding.datatypes.long, scope=response_))
response_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(response_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
response_._ContentModel = pyxb.binding.content.ParticleModel(response_._GroupModel, min_occurs=1, max_occurs=1)



errorResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errors'), CTD_ANON_6, scope=errorResponse_))
errorResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(errorResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
errorResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(errorResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errors')), min_occurs=0L, max_occurs=1)
    )
errorResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(errorResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(errorResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
errorResponse_._ContentModel = pyxb.binding.content.ParticleModel(errorResponse_._GroupModel, min_occurs=1, max_occurs=1)



principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dobVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators))

principalVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ssnVerified'), pyxb.binding.datatypes.boolean, scope=principalVerificationIndicators))
principalVerificationIndicators._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ssnVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dobVerified')), min_occurs=1, max_occurs=1)
    )
principalVerificationIndicators._ContentModel = pyxb.binding.content.ParticleModel(principalVerificationIndicators._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential'), paypageCredential, scope=CTD_ANON_))
CTD_ANON_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageCredential')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_._GroupModel, min_occurs=1, max_occurs=1)



principalAddress._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'countryCode'), STD_ANON_, scope=principalAddress))
principalAddress._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stateProvince')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), min_occurs=1, max_occurs=1)
    )
principalAddress._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalAddress._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'countryCode')), min_occurs=1, max_occurs=1)
    )
principalAddress._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalAddress._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalAddress._GroupModel_2, min_occurs=1, max_occurs=1)
    )
principalAddress._ContentModel = pyxb.binding.content.ParticleModel(principalAddress._GroupModel, min_occurs=1, max_occurs=1)



backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckDecisionNotes'), pyxb.binding.datatypes.string, scope=backgroundCheckResults_))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lienResult'), lienResult, scope=backgroundCheckResults_))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'business'), businessResult, scope=backgroundCheckResults_))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principal'), principalResult, scope=backgroundCheckResults_))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyData'), bankruptcyResult, scope=backgroundCheckResults_))

backgroundCheckResults_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'businessToPrincipalAssociation'), businessToPrincipalAssociation, scope=backgroundCheckResults_))
backgroundCheckResults_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'business')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principal')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'businessToPrincipalAssociation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckDecisionNotes')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyData')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(backgroundCheckResults_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lienResult')), min_occurs=0L, max_occurs=1)
    )
backgroundCheckResults_._ContentModel = pyxb.binding.content.ParticleModel(backgroundCheckResults_._GroupModel, min_occurs=1, max_occurs=1)



legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxId'), STD_ANON_18, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards'), pyxb.binding.datatypes.boolean, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address'), address, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityType'), legalEntityType, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), STD_ANON_20, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PCI'), legalEntityPciInfo, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs'), STD_ANON_15, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityName'), STD_ANON_50, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume'), pyxb.binding.datatypes.string, scope=legalEntityCreateRequest_))

legalEntityCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principals'), CTD_ANON_3, scope=legalEntityCreateRequest_))
legalEntityCreateRequest_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactPhone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PCI')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principals')), min_occurs=0L, max_occurs=1)
    )
legalEntityCreateRequest_._ContentModel = pyxb.binding.content.ParticleModel(legalEntityCreateRequest_._GroupModel, min_occurs=1, max_occurs=1)



legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults'), backgroundCheckResults_, scope=legalEntityCreateResponse_))

legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), pyxb.binding.datatypes.short, scope=legalEntityCreateResponse_))

legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId'), pyxb.binding.datatypes.string, scope=legalEntityCreateResponse_))

legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principals'), CTD_ANON_5, scope=legalEntityCreateResponse_))

legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseDescription'), pyxb.binding.datatypes.string, scope=legalEntityCreateResponse_))

legalEntityCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalLegalEntity'), legalEntityRetrievalResponse_, scope=legalEntityCreateResponse_))
legalEntityCreateResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
legalEntityCreateResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principals')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseDescription')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalLegalEntity')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults')), min_occurs=0L, max_occurs=1)
    )
legalEntityCreateResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
legalEntityCreateResponse_._ContentModel = pyxb.binding.content.ParticleModel(legalEntityCreateResponse_._GroupModel, min_occurs=1, max_occurs=1)



potentialRiskIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=potentialRiskIndicator))

potentialRiskIndicator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), riskIndicatorCode, scope=potentialRiskIndicator))
potentialRiskIndicator._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(potentialRiskIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(potentialRiskIndicator._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
potentialRiskIndicator._ContentModel = pyxb.binding.content.ParticleModel(potentialRiskIndicator._GroupModel, min_occurs=1, max_occurs=1)



legalEntityPrincipalUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), STD_ANON_42, scope=legalEntityPrincipalUpdatable_))

legalEntityPrincipalUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), principalAddressUpdatable, scope=legalEntityPrincipalUpdatable_))

legalEntityPrincipalUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), STD_ANON_39, scope=legalEntityPrincipalUpdatable_))
legalEntityPrincipalUpdatable_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityPrincipalUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'emailAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipalUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactPhone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipalUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable')), min_occurs=0L, max_occurs=1)
    )
legalEntityPrincipalUpdatable_._ContentModel = pyxb.binding.content.ParticleModel(legalEntityPrincipalUpdatable_._GroupModel, min_occurs=1, max_occurs=1)



businessResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verificationResult'), businessVerificationResult, scope=businessResult))
businessResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verificationResult')), min_occurs=0L, max_occurs=1)
    )
businessResult._ContentModel = pyxb.binding.content.ParticleModel(businessResult._GroupModel, min_occurs=1, max_occurs=1)



subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'createCredentials'), pyxb.binding.datatypes.boolean, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber'), STD_ANON_14, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount'), pyxb.binding.datatypes.string, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pspMerchantId'), STD_ANON_10, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName'), STD_ANON_47, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber'), STD_ANON_8, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexMid'), STD_ANON_46, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'purchaseCurrency'), STD_ANON_6, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address'), address, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber'), STD_ANON_2, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor'), STD_ANON_27, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'primaryContact'), subMerchantPrimaryContact, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor'), STD_ANON_36, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid'), STD_ANON_13, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantCategoryCode'), STD_ANON_32, scope=subMerchantCreateRequest_))

subMerchantCreateRequest_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantName'), STD_ANON_49, scope=subMerchantCreateRequest_))
subMerchantCreateRequest_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'purchaseCurrency')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantCategoryCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pspMerchantId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'primaryContact')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createCredentials')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor')), min_occurs=0L, max_occurs=1)
    )
subMerchantCreateRequest_._ContentModel = pyxb.binding.content.ParticleModel(subMerchantCreateRequest_._GroupModel, min_occurs=1, max_occurs=1)



subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), pyxb.binding.datatypes.dateTime, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId'), pyxb.binding.datatypes.string, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'disabled'), pyxb.binding.datatypes.boolean, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString'), pyxb.binding.datatypes.string, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credentials'), subMerchantCredentials, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), pyxb.binding.datatypes.string, scope=subMerchantRetrievalResponse_))

subMerchantRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials'), CTD_ANON, scope=subMerchantRetrievalResponse_))
subMerchantRetrievalResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'purchaseCurrency')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantCategoryCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pspMerchantId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'primaryContact')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'createCredentials')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor')), min_occurs=0L, max_occurs=1)
    )
subMerchantRetrievalResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'disabled')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credentials')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updateDate')), min_occurs=0L, max_occurs=1)
    )
subMerchantRetrievalResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
subMerchantRetrievalResponse_._ContentModel = pyxb.binding.content.ParticleModel(subMerchantRetrievalResponse_._GroupModel, min_occurs=1, max_occurs=1)



subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber'), STD_ANON_19, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid'), STD_ANON_5, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'primaryContact'), subMerchantPrimaryContact, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'disable'), pyxb.binding.datatypes.boolean, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount'), pyxb.binding.datatypes.string, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor'), STD_ANON_25, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber'), STD_ANON_30, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), STD_ANON_44, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'amexMid'), STD_ANON_51, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), addressUpdatable, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber'), STD_ANON_23, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor'), STD_ANON_37, scope=subMerchantUpdatable_))

subMerchantUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName'), STD_ANON_34, scope=subMerchantUpdatable_))
subMerchantUpdatable_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'amexMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'discoverConveyedMid')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'customerServiceNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hardCodedBillingDescriptor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'maxTransactionAmount')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankRoutingNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankAccountNumber')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'primaryContact')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'disable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckCompanyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eCheckBillingDescriptor')), min_occurs=0L, max_occurs=1)
    )
subMerchantUpdatable_._ContentModel = pyxb.binding.content.ParticleModel(subMerchantUpdatable_._GroupModel, min_occurs=1, max_occurs=1)



principalResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verificationResult'), principalVerificationResult, scope=principalResult))
principalResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verificationResult')), min_occurs=0L, max_occurs=1)
    )
principalResult._ContentModel = pyxb.binding.content.ParticleModel(principalResult._GroupModel, min_occurs=1, max_occurs=1)



bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip4'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyCount'), pyxb.binding.datatypes.int, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'filingDate'), pyxb.binding.datatypes.date, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'companyName'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), pyxb.binding.datatypes.string, scope=bankruptcyResult))

bankruptcyResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyType'), pyxb.binding.datatypes.string, scope=bankruptcyResult))
bankruptcyResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bankruptcyCount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'companyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip4')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(bankruptcyResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'filingDate')), min_occurs=0L, max_occurs=1)
    )
bankruptcyResult._ContentModel = pyxb.binding.content.ParticleModel(bankruptcyResult._GroupModel, min_occurs=1, max_occurs=1)



businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cityVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stateVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxIdVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))

businessVerificationIndicators._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zipVerified'), pyxb.binding.datatypes.boolean, scope=businessVerificationIndicators))
businessVerificationIndicators._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cityVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stateVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zipVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phoneVerified')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationIndicators._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxIdVerified')), min_occurs=1, max_occurs=1)
    )
businessVerificationIndicators._ContentModel = pyxb.binding.content.ParticleModel(businessVerificationIndicators._GroupModel, min_occurs=1, max_occurs=1)



legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transactionId'), pyxb.binding.datatypes.string, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseCode'), pyxb.binding.datatypes.short, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId'), pyxb.binding.datatypes.string, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'decisionDate'), pyxb.binding.datatypes.dateTime, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'responseDescription'), pyxb.binding.datatypes.string, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'updateDate'), pyxb.binding.datatypes.dateTime, scope=legalEntityRetrievalResponse_))

legalEntityRetrievalResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults'), backgroundCheckResults_, scope=legalEntityRetrievalResponse_))
legalEntityRetrievalResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxId')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactPhone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PCI')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principals')), min_occurs=0L, max_occurs=1)
    )
legalEntityRetrievalResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legalEntityId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseCode')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'responseDescription')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backgroundCheckResults')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'updateDate')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'decisionDate')), min_occurs=0L, max_occurs=1)
    )
legalEntityRetrievalResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
legalEntityRetrievalResponse_._ContentModel = pyxb.binding.content.ParticleModel(legalEntityRetrievalResponse_._GroupModel, min_occurs=1, max_occurs=1)



lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'releasedCount'), pyxb.binding.datatypes.int, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unreleasedCount'), pyxb.binding.datatypes.int, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'filingDate'), pyxb.binding.datatypes.date, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'companyName'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'state'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lienType'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), pyxb.binding.datatypes.string, scope=lienResult))

lienResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zip4'), pyxb.binding.datatypes.string, scope=lienResult))
lienResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lienType')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'releasedCount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unreleasedCount')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'companyName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'state')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zip4')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(lienResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'filingDate')), min_occurs=0L, max_occurs=1)
    )
lienResult._ContentModel = pyxb.binding.content.ParticleModel(lienResult._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator'), potentialRiskIndicator, scope=CTD_ANON_2))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=1, max_occurs=1)



businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators'), CTD_ANON_7, scope=businessVerificationResult))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation'), businessNameAddressPhoneAssociation, scope=businessVerificationResult))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators'), businessVerificationIndicators, scope=businessVerificationResult))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameAddressTaxIdAssociation'), nameAddressTaxIdAssociation, scope=businessVerificationResult))

businessVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overallScore'), businessScore, scope=businessVerificationResult))
businessVerificationResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overallScore')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameAddressTaxIdAssociation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators')), min_occurs=0L, max_occurs=1)
    )
businessVerificationResult._ContentModel = pyxb.binding.content.ParticleModel(businessVerificationResult._GroupModel, min_occurs=1, max_occurs=1)



paypageCredential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageId'), pyxb.binding.datatypes.string, scope=paypageCredential))

paypageCredential._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'username'), pyxb.binding.datatypes.string, scope=paypageCredential))
paypageCredential._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(paypageCredential._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'username')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(paypageCredential._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageId')), min_occurs=0L, max_occurs=1)
    )
paypageCredential._ContentModel = pyxb.binding.content.ParticleModel(paypageCredential._GroupModel, min_occurs=1, max_occurs=1)



principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators'), CTD_ANON_2, scope=principalVerificationResult))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation'), principalNameAddressPhoneAssociation, scope=principalVerificationResult))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators'), principalVerificationIndicators, scope=principalVerificationResult))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overallScore'), principalScore, scope=principalVerificationResult))

principalVerificationResult._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nameAddressSsnAssociation'), nameAddressSsnAssociation, scope=principalVerificationResult))
principalVerificationResult._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overallScore')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameAddressSsnAssociation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nameAddressPhoneAssociation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'verificationIndicators')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalVerificationResult._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskIndicators')), min_occurs=0L, max_occurs=1)
    )
principalVerificationResult._ContentModel = pyxb.binding.content.ParticleModel(principalVerificationResult._GroupModel, min_occurs=1, max_occurs=1)



legalEntityPrincipalCreateResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), pyxb.binding.datatypes.string, scope=legalEntityPrincipalCreateResponse))

legalEntityPrincipalCreateResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipalCreateResponse))

legalEntityPrincipalCreateResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), pyxb.binding.datatypes.string, scope=legalEntityPrincipalCreateResponse))
legalEntityPrincipalCreateResponse._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityPrincipalCreateResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principalId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipalCreateResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipalCreateResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), min_occurs=0L, max_occurs=1)
    )
legalEntityPrincipalCreateResponse._ContentModel = pyxb.binding.content.ParticleModel(legalEntityPrincipalCreateResponse._GroupModel, min_occurs=1, max_occurs=1)



addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2'), STD_ANON_43, scope=addressUpdatable))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stateProvince'), STD_ANON_38, scope=addressUpdatable))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), STD_ANON_22, scope=addressUpdatable))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1'), STD_ANON_3, scope=addressUpdatable))

addressUpdatable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postalCode'), STD_ANON_33, scope=addressUpdatable))
addressUpdatable._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stateProvince')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(addressUpdatable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), min_occurs=1, max_occurs=1)
    )
addressUpdatable._ContentModel = pyxb.binding.content.ParticleModel(addressUpdatable._GroupModel, min_occurs=1, max_occurs=1)



address._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'countryCode'), STD_ANON_26, scope=address))
address._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress1')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'streetAddress2')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stateProvince')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postalCode')), min_occurs=1, max_occurs=1)
    )
address._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(address._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'countryCode')), min_occurs=1, max_occurs=1)
    )
address._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(address._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(address._GroupModel_2, min_occurs=1, max_occurs=1)
    )
address._ContentModel = pyxb.binding.content.ParticleModel(address._GroupModel, min_occurs=1, max_occurs=1)



subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'credentials'), subMerchantCredentials, scope=subMerchantCreateResponse_))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalSubMerchant'), subMerchantRetrievalResponse_, scope=subMerchantCreateResponse_))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId'), pyxb.binding.datatypes.string, scope=subMerchantCreateResponse_))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials'), CTD_ANON_, scope=subMerchantCreateResponse_))

subMerchantCreateResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString'), pyxb.binding.datatypes.string, scope=subMerchantCreateResponse_))
subMerchantCreateResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
subMerchantCreateResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subMerchantId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantIdentString')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalSubMerchant')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'credentials')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'paypageCredentials')), min_occurs=0L, max_occurs=1)
    )
subMerchantCreateResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
subMerchantCreateResponse_._ContentModel = pyxb.binding.content.ParticleModel(subMerchantCreateResponse_._GroupModel, min_occurs=1, max_occurs=1)



legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pciLevel'), STD_ANON_29, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'qualifiedSecurityAssessor'), STD_ANON_52, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'isExclusiveToPsp'), pyxb.binding.datatypes.boolean, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reportOnCompliance'), pyxb.binding.datatypes.date, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mostRecentlyPassedScan'), pyxb.binding.datatypes.date, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scanningVendor'), STD_ANON_45, scope=legalEntityPciInfo))

legalEntityPciInfo._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'isPciComplianceValidated'), pyxb.binding.datatypes.boolean, scope=legalEntityPciInfo))
legalEntityPciInfo._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'isExclusiveToPsp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'isPciComplianceValidated')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scanningVendor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'qualifiedSecurityAssessor')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mostRecentlyPassedScan')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reportOnCompliance')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPciInfo._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pciLevel')), min_occurs=1, max_occurs=1)
    )
legalEntityPciInfo._ContentModel = pyxb.binding.content.ParticleModel(legalEntityPciInfo._GroupModel, min_occurs=1, max_occurs=1)



nameAddressSsnAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=nameAddressSsnAssociation))

nameAddressSsnAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), nameAddressSsnAssociationCode, scope=nameAddressSsnAssociation))
nameAddressSsnAssociation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nameAddressSsnAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(nameAddressSsnAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
nameAddressSsnAssociation._ContentModel = pyxb.binding.content.ParticleModel(nameAddressSsnAssociation._GroupModel, min_occurs=1, max_occurs=1)



principalNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=principalNameAddressPhoneAssociation))

principalNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), principalNameAddressPhoneAssociationCode, scope=principalNameAddressPhoneAssociation))
principalNameAddressPhoneAssociation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
principalNameAddressPhoneAssociation._ContentModel = pyxb.binding.content.ParticleModel(principalNameAddressPhoneAssociation._GroupModel, min_occurs=1, max_occurs=1)



legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), pyxb.binding.datatypes.date, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), STD_ANON_53, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ssn'), STD_ANON_7, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'driversLicense'), STD_ANON_40, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), STD_ANON_54, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'driversLicenseState'), STD_ANON_35, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), STD_ANON_11, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principalId'), pyxb.binding.datatypes.int, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), STD_ANON_55, scope=legalEntityPrincipal))

legalEntityPrincipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'address'), principalAddress, scope=legalEntityPrincipal))
legalEntityPrincipal._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principalId')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'emailAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ssn')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactPhone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'driversLicense')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'driversLicenseState')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityPrincipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'address')), min_occurs=0L, max_occurs=1)
    )
legalEntityPrincipal._ContentModel = pyxb.binding.content.ParticleModel(legalEntityPrincipal._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principal'), legalEntityPrincipal, scope=CTD_ANON_3))
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principal')), min_occurs=1L, max_occurs=1L)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=1, max_occurs=1)



legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable'), addressUpdatable, scope=legalEntityUpdatable_))

legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactPhone'), STD_ANON_48, scope=legalEntityUpdatable_))

legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume'), pyxb.binding.datatypes.string, scope=legalEntityUpdatable_))

legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards'), pyxb.binding.datatypes.boolean, scope=legalEntityUpdatable_))

legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PCI'), legalEntityPciInfo, scope=legalEntityUpdatable_))

legalEntityUpdatable_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs'), STD_ANON_28, scope=legalEntityUpdatable_))
legalEntityUpdatable_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressUpdatable')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PCI')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactPhone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doingBusinessAs')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'annualCreditCardSalesVolume')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(legalEntityUpdatable_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hasAcceptedCreditCards')), min_occurs=1, max_occurs=1)
    )
legalEntityUpdatable_._ContentModel = pyxb.binding.content.ParticleModel(legalEntityUpdatable_._GroupModel, min_occurs=1, max_occurs=1)



approvedMccResponse_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedMccs'), CTD_ANON_4, scope=approvedMccResponse_))
approvedMccResponse_._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(approvedMccResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transactionId')), min_occurs=0L, max_occurs=1)
    )
approvedMccResponse_._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(approvedMccResponse_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedMccs')), min_occurs=0L, max_occurs=1)
    )
approvedMccResponse_._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(approvedMccResponse_._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(approvedMccResponse_._GroupModel_2, min_occurs=1, max_occurs=1)
    )
approvedMccResponse_._ContentModel = pyxb.binding.content.ParticleModel(approvedMccResponse_._GroupModel, min_occurs=1, max_occurs=1)



nameAddressTaxIdAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=nameAddressTaxIdAssociation))

nameAddressTaxIdAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), nameAddressTaxIdAssociationCode, scope=nameAddressTaxIdAssociation))
nameAddressTaxIdAssociation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(nameAddressTaxIdAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(nameAddressTaxIdAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
nameAddressTaxIdAssociation._ContentModel = pyxb.binding.content.ParticleModel(nameAddressTaxIdAssociation._GroupModel, min_occurs=1, max_occurs=1)



subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'passwordExpirationDate'), pyxb.binding.datatypes.dateTime, scope=subMerchantCredentials))

subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'username'), pyxb.binding.datatypes.string, scope=subMerchantCredentials))

subMerchantCredentials._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'password'), pyxb.binding.datatypes.string, scope=subMerchantCredentials))
subMerchantCredentials._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'username')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'password')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantCredentials._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'passwordExpirationDate')), min_occurs=0L, max_occurs=1)
    )
subMerchantCredentials._ContentModel = pyxb.binding.content.ParticleModel(subMerchantCredentials._GroupModel, min_occurs=1, max_occurs=1)



businessNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=businessNameAddressPhoneAssociation))

businessNameAddressPhoneAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), businessNameAddressPhoneAssociationCode, scope=businessNameAddressPhoneAssociation))
businessNameAddressPhoneAssociation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessNameAddressPhoneAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
businessNameAddressPhoneAssociation._ContentModel = pyxb.binding.content.ParticleModel(businessNameAddressPhoneAssociation._GroupModel, min_occurs=1, max_occurs=1)



subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), STD_ANON_4, scope=subMerchantPrimaryContact))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'emailAddress'), STD_ANON_16, scope=subMerchantPrimaryContact))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), STD_ANON_17, scope=subMerchantPrimaryContact))

subMerchantPrimaryContact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), STD_ANON_21, scope=subMerchantPrimaryContact))
subMerchantPrimaryContact._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'emailAddress')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(subMerchantPrimaryContact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), min_occurs=1, max_occurs=1)
    )
subMerchantPrimaryContact._ContentModel = pyxb.binding.content.ParticleModel(subMerchantPrimaryContact._GroupModel, min_occurs=1, max_occurs=1)



principalScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=principalScore))

principalScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), principalOverallScore, scope=principalScore))
principalScore._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(principalScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(principalScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
principalScore._ContentModel = pyxb.binding.content.ParticleModel(principalScore._GroupModel, min_occurs=1, max_occurs=1)



businessToPrincipalAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=businessToPrincipalAssociation))

businessToPrincipalAssociation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), businessToPrincipalScore, scope=businessToPrincipalAssociation))
businessToPrincipalAssociation._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessToPrincipalAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessToPrincipalAssociation._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
businessToPrincipalAssociation._ContentModel = pyxb.binding.content.ParticleModel(businessToPrincipalAssociation._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approvedMcc'), pyxb.binding.datatypes.string, scope=CTD_ANON_4))
CTD_ANON_4._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approvedMcc')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_4._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'principal'), legalEntityPrincipalCreateResponse, scope=CTD_ANON_5))
CTD_ANON_5._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'principal')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_5._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_5._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'error'), pyxb.binding.datatypes.string, scope=CTD_ANON_6))
CTD_ANON_6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'error')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_6._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_6._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator'), potentialRiskIndicator, scope=CTD_ANON_7))
CTD_ANON_7._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'riskIndicator')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_7._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_7._GroupModel, min_occurs=1, max_occurs=1)



businessScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=businessScore))

businessScore._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'score'), businessOverallScore, scope=businessScore))
businessScore._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(businessScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'score')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(businessScore._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), min_occurs=0L, max_occurs=1)
    )
businessScore._ContentModel = pyxb.binding.content.ParticleModel(businessScore._GroupModel, min_occurs=1, max_occurs=1)

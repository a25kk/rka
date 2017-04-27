# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from rka.sitecontent.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of rka.sitecontent into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rka.sitecontent is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.rkaroductInstalled('rka.sitecontent'))

    def test_uninstall(self):
        """Test if rka.sitecontent is cleanly uninstalled."""
        self.installer.uninstallProducts(['rka.sitecontent'])
        self.assertFalse(self.installer.rkaroductInstalled('rka.sitecontent'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IRkaSitecontentLayer is registered."""
        from rka.sitecontent.interfaces import IRkaSitecontentLayer
        from plone.browserlayer import utils
        self.failUnless(IRkaSitecontentLayer in utils.registered_layers())

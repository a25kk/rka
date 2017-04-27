# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from rka.buildout.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of rka.buildout into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rka.buildout is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('rka.buildout'))

    def test_uninstall(self):
        """Test if rka.buildout is cleanly uninstalled."""
        self.installer.uninstallProducts(['rka.buildout'])
        self.assertFalse(self.installer.isProductInstalled('rka.buildout'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IRkaBuildoutLayer is registered."""
        from rka.buildout.interfaces import IRkaBuildoutLayer
        from plone.browserlayer import utils
        self.failUnless(IRkaBuildoutLayer in utils.registered_layers())

def test_scdeployscripts_package(host):
    package= host.package("seachange-deploy-scripts-2.3.0-0737.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_ismmmccomponents_package(host):
    package= host.package("seachange-ism-mmc-components-2.3.0-0075.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_platformupdate_package(host):
    package= host.package("seachange-platform-update-10.0.2.0-0010.el6.x86_64")
    assert package.is_installed
    assert package.version.startswith("10.0.2")

def test_mmc_package(host):
    package= host.package("seachange-mmc-2.3.0-0737.x86_64")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_mmchelp_package(host):
    package= host.package("seachange-mmc_help-2.3.0-0737.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_rhqplugins_package(host):
    package= host.package("seachange-mmc_help-2.3.0-0737.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_infusionmmc_package(host):
    package= host.package("seachange-infusion-mmc-components-6.0.0-0998.noarch")
    assert package.is_installed
    assert package.version.startswith("6.0.0")

def test_sclinuxconfigscripts_package(host):
    package= host.package("seachange-linux-configuration-scripts-10.0.2.0-0010.el6.noarch")
    assert package.is_installed
    assert package.version.startswith("10.0.2")

def test_rhqtools_package(host):
    package= host.package("seachange-rhq-tools-2.3.0-0737.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

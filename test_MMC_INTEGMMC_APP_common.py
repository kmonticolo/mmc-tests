# userzy uslugi procesy pliki filesystemy centos

def test_uname_output(Command):
    command = Command('uname -s')
    assert command.stdout.rstrip() == 'Linux'
    assert command.rc == 0

def test_resolv(File):
    resolv= File("/etc/resolv.conf")
    assert resolv.user == "root"
    assert resolv.group == "root"
    assert resolv.mode == 0o644
    assert resolv.contains("nameserver 128.168.160.95")

def test_visudo(Command):
    command = Command('sudo visudo -cf /etc/sudoers')
    assert command.rc == 0

def test_ntp_conf(File):
    ntp_conf= File("/etc/ntp.conf")
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o644
    assert ntp_conf.contains("server 128.168.160.95") or ntp_conf.contains("server 128.168.51.55")

def test_NTP_ntpstat(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_root_user(host):
    user = host.user("root")
    assert user.exists
    assert user.uid == 0
    assert user.gid == 0
    assert user.name == "root"
    assert user.group == "root"
    assert user.groups == [ "root" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/root"

def test_seachange_user(host):
    user = host.user("seachange")
    assert user.exists
    assert user.uid == 500
    assert user.gid == 500
    assert user.name == "seachange"
    assert user.group == "seachange"
    assert user.groups == [ "seachange", "wheel" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/home/seachange"

def test_seachange_group_exists(Group):
    group = Group('seachange')
    assert group.exists

def test_ntpd_service_exists(host):
    service = host.service("ntpd")
    assert service.is_running
    assert service.is_enabled

def test_zabbix_conf(File):
    zabbix_conf= File("/etc/zabbix/zabbix_agentd.conf")
    assert zabbix_conf.user == "root"
    assert zabbix_conf.group == "root"
    assert zabbix_conf.mode == 0o644
    assert zabbix_conf.contains("172.16.160.24") or zabbix_conf.contains("128.168.160.24")


def test_zabbix_agent_service_exists(host):
    service = host.service("zabbix-agent")
    assert service.is_running
    assert service.is_enabled

def test_vmware_tools_service_exists(host):
    service = host.service("vmware-tools")
    assert service.is_running
    assert service.is_enabled

def test_rhq_agent_running(Command):
    command = Command('sudo service rhq-agent status')
    assert command.rc == 0

def test_rhq_server_running(Command):
    command = Command('sudo service rhq-server status')
    assert command.rc == 0

#def test_network_configured_devices(Command):
#def test_network_configured_devices(Command):
#    #command = Command('service network status|grep -A1 ^Configured|grep "lo eth0"')
#    command = Command('service network status|grep -A1 ^Configured"')
#    assert command.rc == 0

#def test_network_currently_active_devices(Command):
#    command = Command('service network status|grep -A1 ^Currently\ active|grep "lo eth0"')
#    assert command.rc == 0

def test_mmc_service_exists(host):
    service = host.service("mmc")
    assert service.is_running
    assert service.is_enabled

def test_redis_sentinel_service_exists(host):
    service = host.service("redis-sentinel")
    assert service.is_running
    assert service.is_enabled

def test_rhq_server_service_exists(host):
    service = host.service("rhq-server")
    assert service.is_running
    assert service.is_enabled

def test_jexec_service_exists(host):
    service = host.service("jexec")
    assert service.is_running
    assert service.is_enabled

def test_apachectl_syntax_output(Command):
    command = Command('/usr/sbin/apachectl -t')
def test_apachectl_syntax_output(Command):
    command = Command('/usr/sbin/apachectl -t')
def test_apachectl_syntax_output(Command):
    command = Command('/usr/sbin/apachectl -t')
def test_apachectl_syntax_output(Command):
    command = Command('/usr/sbin/apachectl -t')
def test_apachectl_syntax_output(Command):
    command = Command('/usr/sbin/apachectl -t')
    assert command.rc == 0

def test_tomcat_package(host):
    package= host.package("apache-tomcat-6.0.32-jdk6.1054")
    assert package.is_installed
    assert package.version.startswith("6.0.32")

def test_sun_jdk_package(host):
    package= host.package("sun-jdk-1.6.0_21-1054.x86_64")
    assert package.is_installed
    assert package.version.startswith("1.6.0")

def test_sun_jre_package(host):
    package= host.package("sun-jre-1.6.0.24-jdk6.1138")
    assert package.is_installed
    assert package.version.startswith("1.6.0")

def test_jboss_package(host):
    package= host.package("jboss-5.1.0.GA-1098.noarch")
    assert package.is_installed
    assert package.version.startswith("5.1.0")


def test_rsyslog_package(host):
    package= host.package("seachange-rsyslog-client-2.3.0-0711.noarch")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_tomcat_spring_scc_xml(File):
    scc= File("/seachange/local/apache-tomcat-6.0.32/webapps/pcs/WEB-INF/classes/spring-scc.xml")
    assert scc.user == "seachange"
    assert scc.group == "root"
    assert scc.mode == 0o644
    assert scc.contains("tv.seachange.advads.scc.StreamControlClientContextEmulator")
    assert scc.contains("tv.seachange.advads.scc.manager.SessionCacheManagerEmulator")

def test_seachange_yum_repo(File):
    scc= File("/etc/yum.repos.d/SeaChange.repo")
    assert scc.user == "seachange"
    assert scc.group == "seachange"
    assert scc.mode == 0o644
    assert scc.contains("baseurl = http://localhost/seachange/thirdparty-repository")
    assert scc.contains("enabled = 1")

def test_adr_war(File):
    adr= File("/seachange/local/adr-latest/webapps/adr.war")
    assert adr.user == "seachange"
    assert adr.group == "root"
    assert adr.mode == 0o644

def test_ads_war(File):
    ads= File("/seachange/local/ads-latest/webapps/ads.war")
    assert ads.user == "seachange"
    assert ads.group == "root"
    assert ads.mode == 0o644

def test_pcs_war(File):
    scc= File("/seachange/local/pcs-latest/webapps/pcs.war")
    assert scc.user == "seachange"
    assert scc.group == "root"
    assert scc.mode == 0o644

def test_ssh_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
        "tcp://22",
        "tcp://0.0.0.0:22",
        "tcp://127.0.0.1:22",
        "tcp://:::22",
        "tcp://::1:22",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

#def test_app_socket(host):
#    listening = host.socket.get_listening_sockets()
#    for spec in (
#        "tcp://127.0.0.1:32000",
#    ):
#        socket = host.socket(spec)
#        assert socket.is_listening

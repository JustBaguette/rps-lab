from setuptools import find_packages, setup

package_name = 'ayaya_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = ayaya_pkg.ayanode:main",
            "pusher = ayaya_pkg.robot_news_station:main",
            "ros_rad = ayaya_pkg.robo_stat:main",
            "rob_listener = ayaya_pkg.listening:main"
        ],
    },
)

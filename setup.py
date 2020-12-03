import setuptools

setuptools.setup(
    name='backup-to-s3',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/backup-to-s3']
)

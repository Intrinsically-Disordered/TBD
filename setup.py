import sys
from pathlib import Path
from setuptools import setup


if __name__ == '__main__':
    base_dir = Path(__file__).parent
    src_dir = base_dir/'tbd'

    sys.path.insert(0, src_dir.as_posix())
    import __about__ as about

    install_requirements = [
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn',
        'tensorflow',
    ]

    test_requirements = [
        'pytest',
    ]

    doc_requirements = []

    setup(name=about.__title__,
          version=about.__version__,

          description=about.__summary__,
          license=about.__license__,
          url=about.__uri__,

          author=about.__author__,
          author_email=about.__email__,

          package_dir={'tbd': 'tbd'},
          # packages=find_packages(),
          packages=['tbd'],
          include_package_data=True,

          install_requires=install_requirements,
          tests_require=test_requirements,
          extras_require={
              'docs': doc_requirements,
              'test': test_requirements,
              'dev': doc_requirements + test_requirements
          },
          zip_safe=False,)

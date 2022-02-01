SPHINXDIR = ${HOME}/sphinx
PROJECTNAME = richcat
PROJECTDIR = ${HOME}/${PROJECTNAME}
DEPLOYDIR = ${HOME}/docs


.PHONY: apidoc
apidoc:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"

.PHONY: autobuild
autobuild:
	sphinx-autobuild --host 0.0.0.0 -b html "${SPHINXDIR}" "${SPHINXDIR}"/_build

.PHONY: public
public:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "./sphinx" "./richcat"
	sphinx-build -b html "./sphinx" "./docs"
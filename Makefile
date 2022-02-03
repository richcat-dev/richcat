SPHINXDIR = sphinx
PROJECTNAME = richcat
PROJECTDIR = ${PROJECTNAME}
DEPLOYDIR = ${SPHINXDIR}/_build


.PHONY: sphinx-apidoc
sphinx-apidoc:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"

.PHONY: sphinx-autobuild
sphinx-autobuild:
	sphinx-autobuild --host 0.0.0.0 -b html "${SPHINXDIR}" "${DEPLOYDIR}"

.PHONY: sphinx-deploy
sphinx-deploy:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"
	sphinx-build -b html "${SPHINXDIR}" "${DEPLOYDIR}"
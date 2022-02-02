SPHINXDIR = sphinx
PROJECTNAME = richcat
PROJECTDIR = ${PROJECTNAME}
DEPLOYDIR = ${SPHINXDIR}/_build


.PHONY: apidoc
apidoc:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"

.PHONY: autobuild
autobuild:
	sphinx-autobuild --host 0.0.0.0 -b html "${SPHINXDIR}" "${DEPLOYDIR}"

.PHONY: deploy
deploy:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"
	sphinx-build -b html "${SPHINXDIR}" "${DEPLOYDIR}"
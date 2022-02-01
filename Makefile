SPHINXDIR = ${HOME}/sphinx
PROJECTNAME = richcat
PROJECTDIR = ${HOME}/${PROJECTNAME}


.PHONY: apidoc
apidoc:
	sphinx-apidoc -f -H ${PROJECTNAME} -o "${SPHINXDIR}" "${PROJECTDIR}"

.PHONY: autobuild
autobuild:
	sphinx-autobuild --host 0.0.0.0 -b html "${SPHINXDIR}" "${SPHINXDIR}"/_build
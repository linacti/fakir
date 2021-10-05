BLDDIR=$(shell pwd)
TOPDIR=$(shell dirname ${BLDDIR})
PRJDIR=$(TOPDIR)/app
LOGDIR=$(TOPDIR)/logs
RUNDIR=$(TOPDIR)/run
PYDIR=$(TOPDIR)/py
REQ=${PRJDIR}/requirements.txt
LIBDIR=$(PYDIR)/lib
PYTHON=$(PYDIR)/bin/python3
PIP=$(PYDIR)/bin/pip3
UNAME=$(shell uname)
BRANCH=$(shell git branch 2>/dev/null | grep '^*' | colrm 1 2)
PATH=$(NODEDIR)/bin:$(PYDIR)/bin:$(PRJDIR)/bin:/bin:/usr/bin


all:   done.python done.dirs done.gecko done.chrome done.pre done.pip

clean:
	rm -f done.*

distclean: clean
	rm -rf Python-* geckodriver* chromedriver*


python: done.python
dirs: done.dirs
pip: done.pip
pre: done.pre
req: done.req
gecko: done.gecko
chrome: done.chrome

Python-${pythonversion}.tgz:
	curl -O https://www.python.org/ftp/python/${pythonversion}/Python-${pythonversion}.tgz
	touch $@

Python-${pythonversion}: Python-${pythonversion}.tgz
	tar zxf $<
	touch $@

done.python: Python-${pythonversion}
	cd Python-${pythonversion} ; \
	./configure --prefix=$(PYDIR) --enable-optimizations ; \
	make ;\
	make install
	@if [ -x $(PYDIR)/bin/python ] ; then echo "*** Python link already exists. Skipping." ; else ln -s python3 $(PYDIR)/bin/python ; fi
	touch $@

done.pip: done.python
	$(PIP) install --upgrade pip
	touch $@

done.req: done.pip
	${PYDIR}/bin/pip3 install jupyterlab
	if [ -f ${REQ} ]; then $(PIP) install -r ${REQ} ;fi
	touch $@

done.pre: done.req
	@for f in `find .. -name "*.++"`; do  \
		n=`echo $$f | sed "s/.++$$//g"`; \
		echo "$$f => $$n"; \
		if [ -f $$n ] ; then mv $$n $$n.old ; fi; \
		cat $$f \
			| sed "s@++TOPDIR++@$(TOPDIR)@g" \
			| sed "s@++PYDIR++@$(PYDIR)@g" \
			| sed "s@++LIBDIR++@$(LIBDIR)@g" \
			| sed "s@++LOGDIR++@$(LOGDIR)@g" \
			| sed "s@++RUNDIR++@$(RUNDIR)@g" \
			| sed "s@++PRJDIR++@$(PRJDIR)@g" \
			| sed "s@++APPUSER++@$(APPUSER)@g" \
			| sed "s@++APPGROUP++@$(APPGROUP)@g" \
			| sed "s@++DOMAIN++@$(DOMAIN)@g" \
			| sed "s@++APPPORT++@$(APPPORT)@g" \
			| sed "s@++PYTHON++@$(PYTHON)@g" \
			| sed "s@++VERSION++@$(VERSION)@g" \
			| sed "s@++BRANCH++@$(BRANCH)@g" \
			> $$n ; \
		chmod 755 $$n ; \
	done
	touch $@


geckodriver-v${geckodriver}-linux64.tar.gz:
	wget https://github.com/mozilla/geckodriver/releases/download/v${geckodriver}/geckodriver-v${geckodriver}-linux64.tar.gz
	touch $@

done.gecko: done.python geckodriver-v${geckodriver}-linux64.tar.gz
	tar zxvf geckodriver-v${geckodriver}-linux64.tar.gz
	mv geckodriver $(PYDIR)/bin
	touch $@

chromedriver_linux64.zip:
	wget https://chromedriver.storage.googleapis.com/${chromedriver}/chromedriver_linux64.zip
	touch $@

done.chrome: done.python chromedriver_linux64.zip
	unzip chromedriver_linux64.zip
	mv chromedriver $(PYDIR)/bin
	touch $@

done.dirs:
	mkdir -p ${LOGDIR}
	mkdir -p ${RUNDIR}
	touch $@

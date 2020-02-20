CDK = pipenv run npm run cdk --

clean:
	rm -rf cdk.out

setup:
	npm install
	pipenv install

synth: setup
	$(CDK) synth '*'

deploy: setup
	$(CDK) deploy '*'

destroy: setup
	$(CDK) destroy '*'


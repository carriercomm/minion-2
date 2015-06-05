angular.module('Boss', ['ui.bootstrap'])
    .controller('ActuatorController', function($scope, $http) {
        $scope.obj = window.actuator;
        $scope.availableActuatorClasses = _.pluck(window.availableActuators, 'class');
        // Check current one in same loop
        var currentSystems = {};
        _.each(window.availableActuators, function(actuator) {
            if(actuator.class === $scope.obj.class) {
                actuator.configuration = $scope.obj.configuration;
            } else {
                actuator.configuration = _.zipObject(_.pluck(actuator.setup, 'name'),_.pluck(actuator.setup, 'default'));
            }
            currentSystems[actuator.class] = actuator;
        });
        $scope.systems = currentSystems;

        $scope.submit = function() {
            $scope.obj.configuration = currentSystems[$scope.obj.class].configuration;
            _.each($scope.obj.preprocessors, function(p) {
                p.name = p.class;
            });
            $http.post('/save_object/actuators', $scope.obj)
                .then(function(resp){
                    window.alert('Actuator saved successfully');
                })
                .finally(console.debug.bind(console));
        };
    });
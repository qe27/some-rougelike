class ProductionSite:

    def __init__(self, map_object=None, input_mappings={}, output_mappings={}, production_quantity=100):
        # input mapping: {"soil": 100, "rocks": 1000}
        self.map_object = map_object
        self.input_mappings = input_mappings
        self.output_mappings = output_mappings
        self.production_quantity = production_quantity

    def do_production_for_turn(self):
        # TODO: allow multiple type inputs
        # TODO: get input resources not only from current tile
        # TODO: do in transaction
        input_resource = next(iter(self.input_mappings))
        resource_type = input_resource[0]
        expected_quantity = input_resource[1] * self.production_quantity
        # available_quantity =  self.map_object
        structures_by_type = self.map_object.get_structures_by_output_type(resource_type)
        resource_consumed = 0
        for i in structures_by_type:
            if i.quantity_remains >= expected_quantity - resource_consumed:
                i.quantity_remains -= expected_quantity - resource_consumed
                resource_consumed = expected_quantity
                break
            else:
                resource_consumed += i.quantity_remains
                i.quantity_remains = 0

        print('resources consumed: ' + str(resource_consumed))

        output_resource = next(iter(self.output_mappings))
        output_resource_type = output_resource[0]
        output_resource_quantity = resource_consumed * output_resource[0]
        print('output: ' + output_resource_type + 'quantity: ' + str(output_resource_quantity))
        return (output_resource, output_resource_quantity)

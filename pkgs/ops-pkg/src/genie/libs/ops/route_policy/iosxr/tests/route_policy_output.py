''' 
RoutePolicy Genie Ops Object Outputs for IOSXR.
'''


class RoutePolicyOutput(object):

    showRplRoutePolicy = {'NO-EXPORT': 
                            {'description': 'test15',
                             'statements': 
                                {10: 
                                    {'actions': 
                                        {'actions': 'pass',
                                         'set_community_list': 'no-export'},
                                     'conditions': 
                                        {'match_prefix_list': 'NO-EXPORT'}}}},
                          'all-pass': 
                              {'statements': 
                                  {1: 
                                      {'actions': {'actions': 'pass'},
                                       'conditions': {}}}},
                          'allpass': 
                              {'statements': 
                                  {10: 
                                      {'actions': {'actions': 'pass'},
                                       'conditions': {}}}},
                          'as-path': 
                              {'statements': 
                                  {10: {'actions': {}, 
                                        'conditions': {}}}},
                          'aspath': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': 
                                          {'match_as_path_list': 'test'}},
                                   20: 
                                      {'actions': {'actions': 'drop'},
                                       'conditions': {}}}},
                          'test': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'set_route_origin': 'incomplete'},
                                       'conditions': 
                                          {'match_local_pref_eq': '123'}},
                                   20: 
                                      {'actions': {'set_weight': '44'},
                                       'conditions': {'match_med_eq': 100}},
                                   1: 
                                      {'actions': 
                                          {'set_route_origin': 'incomplete'},
                                       'conditions': {}}}},
                          'test-community': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'set_community': ['100:1','200:1','300:1'],
                                           'set_community_no_advertise': True,
                                           'set_community_no_export': True},
                                       'conditions': {}},
                                   20: 
                                      {'actions': 
                                          {'set_community': ['111:1','222:1'],
                                           'set_community_additive': True,
                                           'set_community_no_advertise': True,
                                           'set_ext_community_rt': ['100:1','200:1'],
                                           'set_ext_community_rt_additive': True},
                                       'conditions': {}}}},
                          'test2': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': {'match_origin_eq': 'eg'}},
                                   20: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': 
                                          {'match_nexthop_in': 'prefix-set'}},
                                   30: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': 
                                          {'match_local_pref_eq': '13'}}}},
                          'test3': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': {}},
                                   20: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': 
                                          {'match_area_eq': '1'}},
                                   30: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': 
                                          {'match_prefix_list': 'prefix-set'}},
                                   40: 
                                      {'actions': 
                                          {'actions': 'pass'},
                                       'conditions': {}},
                                   50: {'actions': 
                                          {'set_as_path_prepend': 100,
                                           'set_as_path_prepend_repeat_n': 10,
                                           'set_community': ['100:100'],
                                           'set_community_additive': True,
                                           'set_community_delete': 'test',
                                           'set_community_list': 'test',
                                           'set_community_no_advertise': True,
                                           'set_community_no_export': True,
                                           'set_ext_community_delete': 'test',
                                           'set_ext_community_rt': ['300:1','300:2'],
                                           'set_ext_community_rt_additive': True,
                                           'set_ext_community_soo': '100:100',
                                           'set_ext_community_soo_additive': True,
                                           'set_level': 'level-1-2',
                                           'set_local_pref': 100,
                                           'set_med': 113,
                                           'set_metric': '100',
                                           'set_metric_type': 'type-2',
                                           'set_next_hop': '1.1.1.1',
                                           'set_ospf_metric': '100',
                                           'set_route_origin': 'egp',
                                           'set_tag': '111'},
                                        'conditions': {}}}},
                          'testtest': 
                              {'statements': 
                                  {10: 
                                      {'actions': 
                                          {'set_local_pref': 120,
                                           'set_med': 111,
                                           'set_metric_type': 'type-1',
                                           'set_next_hop': '192.168.1.1'},
                                       'conditions': {'match_med_eq': 10}
                                      }
                                  }
                              }
                          }

    RoutePolicy = {'info':
                    {'NO-EXPORT': 
                      {'description': 'test15',
                       'statements': 
                          {10: 
                              {'actions': 
                                  {'actions': 'pass',
                                   'set_community_list': 'no-export'},
                               'conditions': 
                                  {'match_prefix_list': 'NO-EXPORT'}}}},
                    'all-pass': 
                        {'statements': 
                            {1: 
                                {'actions': {'actions': 'pass'},
                                 'conditions': {}}}},
                    'allpass': 
                        {'statements': 
                            {10: 
                                {'actions': {'actions': 'pass'},
                                 'conditions': {}}}},
                    'as-path': 
                        {'statements': 
                            {10: {'actions': {}, 
                                  'conditions': {}}}},
                    'aspath': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': 
                                    {'match_as_path_list': 'test'}},
                             20: 
                                {'actions': {'actions': 'drop'},
                                 'conditions': {}}}},
                    'test': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'set_route_origin': 'incomplete'},
                                 'conditions': 
                                    {'match_local_pref_eq': '123'}},
                             20: 
                                {'actions': {'set_weight': '44'},
                                 'conditions': {'match_med_eq': 100}},
                             1: 
                                {'actions': 
                                    {'set_route_origin': 'incomplete'},
                                 'conditions': {}}}},
                    'test-community': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'set_community': ['100:1','200:1','300:1'],
                                     'set_community_no_advertise': True,
                                     'set_community_no_export': True},
                                 'conditions': {}},
                             20: 
                                {'actions': 
                                    {'set_community': ['111:1','222:1'],
                                     'set_community_additive': True,
                                     'set_community_no_advertise': True,
                                     'set_ext_community_rt': ['100:1','200:1'],
                                     'set_ext_community_rt_additive': True},
                                 'conditions': {}}}},
                    'test2': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': {'match_origin_eq': 'eg'}},
                             20: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': 
                                    {'match_nexthop_in': 'prefix-set'}},
                             30: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': 
                                    {'match_local_pref_eq': '13'}}}},
                    'test3': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': {}},
                             20: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': 
                                    {'match_area_eq': '1'}},
                             30: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': 
                                    {'match_prefix_list': 'prefix-set'}},
                             40: 
                                {'actions': 
                                    {'actions': 'pass'},
                                 'conditions': {}},
                             50: {'actions': 
                                    {'set_as_path_prepend': 100,
                                     'set_as_path_prepend_repeat_n': 10,
                                     'set_community': ['100:100'],
                                     'set_community_additive': True,
                                     'set_community_delete': 'test',
                                     'set_community_list': 'test',
                                     'set_community_no_advertise': True,
                                     'set_community_no_export': True,
                                     'set_ext_community_delete': 'test',
                                     'set_ext_community_rt': ['300:1','300:2'],
                                     'set_ext_community_rt_additive': True,
                                     'set_ext_community_soo': '100:100',
                                     'set_ext_community_soo_additive': True,
                                     'set_level': 'level-1-2',
                                     'set_local_pref': 100,
                                     'set_med': 113,
                                     'set_metric': '100',
                                     'set_metric_type': 'type-2',
                                     'set_next_hop': '1.1.1.1',
                                     'set_ospf_metric': '100',
                                     'set_route_origin': 'egp',
                                     'set_tag': '111'},
                                  'conditions': {}}}},
                    'testtest': 
                        {'statements': 
                            {10: 
                                {'actions': 
                                    {'set_local_pref': 120,
                                     'set_med': 111,
                                     'set_metric_type': 'type-1',
                                     'set_next_hop': '192.168.1.1'},
                                 'conditions': {'match_med_eq': 10}
                                }
                            }
                        }
                    }
                }

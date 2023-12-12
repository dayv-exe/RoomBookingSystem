from functions.array import append
from heapq import heappush, heappop
import collections
from functions.navigation.graph import Graph
from functions.navigation.node import Node


def _dijkstra(start, end):
    # put nodes in priority queue, ordered by dist
    open_list = []
    start.dist = 0
    cur_node = start
    heappush(open_list, start)
    start.added_to_opened_list = True
    # exit loop if we reach the end and no route found, then no route exists
    while cur_node != end and len(open_list) > 0:
        # add neighbours of current node to open list (if they are not there already)
        # if dist to neighbour < dist so far, update dist and parent
        # use heappop to select new cur_node

        for edge in cur_node.edges:
            calc_dist = cur_node.dist + edge.weight
            if calc_dist < edge.end.dist:
                edge.end.dist = calc_dist
                edge.end.parent = cur_node

            if not edge.end.added_to_opened_list:
                edge.end.added_to_opened_list = True
                heappush(open_list, edge.end)

        cur_node = heappop(open_list)

    route = collections.deque([])
    while cur_node is not None:
        route.appendleft(cur_node.name)  # add to front of deque
        cur_node = cur_node.parent
    return route


def init_graph():
    # region GRAPH SET UP
    southampton = Graph()

    bassett = Node('Bassett')
    southampton.add_node(bassett)

    swaything = Node('Swaything')
    southampton.add_node(swaything)

    university = Node('university')
    southampton.add_node(university)

    highfield = Node('Highfield')
    southampton.add_node(highfield)

    portswood = Node('Portswood')
    southampton.add_node(portswood)

    stadium = Node('stadium')
    southampton.add_node(stadium)

    woolston = Node('Woolston')
    southampton.add_node(woolston)

    railway_station = Node('railway station')
    southampton.add_node(railway_station)

    freemantle = Node('Freemantle')
    southampton.add_node(freemantle)

    ikea = Node('ikea')
    southampton.add_node(ikea)

    milbrook = Node('Milbrook')
    southampton.add_node(milbrook)

    shirley = Node('Shirley')
    southampton.add_node(shirley)

    hospital = Node('hospital')
    southampton.add_node(hospital)

    solent_uni = Node('solent uni')
    southampton.add_node(solent_uni)

    city_center = Node('City Center')
    southampton.add_node(city_center)

    bus_station = Node('bus station')
    southampton.add_node(bus_station)

    shopping_mall = Node('shopping mall')
    southampton.add_node(shopping_mall)

    area_nodes = {'bassett': bassett, 'swaything': swaything, 'highfield': highfield, 'portswood': portswood, 'woolston': woolston, 'freemantle': freemantle, 'milbrook': milbrook, 'shirley': shirley, 'city center': city_center}

    point_of_interest_nodes = {'university': university, 'stadium': stadium, 'ikea': ikea, 'hospital': hospital, 'solent_uni': solent_uni, 'shopping mall': shopping_mall}

    transport_hub_nodes = {'railway station': railway_station, 'bus station': bus_station}

    southampton.add_edge(bassett, swaything, 7)
    southampton.add_edge(swaything, university, 1)
    southampton.add_edge(university, highfield, 2)
    southampton.add_edge(highfield, portswood, 4)

    southampton.add_edge(portswood, city_center, 4)
    southampton.add_edge(city_center, bus_station, 2)
    southampton.add_edge(city_center, shopping_mall, 3)
    southampton.add_edge(city_center, solent_uni, 4)
    southampton.add_edge(bus_station, shirley, 3)
    southampton.add_edge(shopping_mall, freemantle, 4)
    southampton.add_edge(solent_uni, woolston, 4)

    southampton.add_edge(portswood, stadium, 5)
    southampton.add_edge(stadium, woolston, 5)
    southampton.add_edge(woolston, railway_station, 4)
    southampton.add_edge(railway_station, freemantle, 3)
    southampton.add_edge(freemantle, ikea, 2)
    southampton.add_edge(ikea, milbrook, 3)
    southampton.add_edge(milbrook, shirley, 4)
    southampton.add_edge(shirley, hospital, 2)
    southampton.add_edge(hospital, bassett, 2)

    return {'transport_nodes': transport_hub_nodes, 'area_nodes': area_nodes}
    # endregion


def go_to(accommodation_area, transport_hub):
    # accommodation is where the user has selected to stay, get the area the accommodation is located and route to it from transport_hub which can either be the railway or bus station in the area
    nodes = init_graph()
    return _dijkstra(nodes['transport_nodes'][transport_hub], nodes['area_nodes'][accommodation_area])

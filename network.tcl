set numNodes 5
set ns [new Simulator]
set topo [new Topography]
$topo load_flatgrid $numNodes $numNodes
$ns use-scheduler Heap
for {set i 0} {$i < $numNodes} {incr i} {
	set node($i) [$ns node]
	$node($i) set queueSize_ 100
	$node($i) set bw_ 10Mbps
	$node($i) set delay_ 10ms
}
for {set i 0} {$i < $numNodes-1} {incr i} {
	$ns duplex-link $node($i) $node([expr $i+1]) 10Mbps 10ms DropTail 
}
proc finish {} {
	global ns
	$ns flush-trace
	$ns finish
	exit 0
}
$ns run

# Ansor

Three components:
- sampling from hierarchical representation
- fine tune via evolutionary search + cost model
- task scheduler to optimise subgraphs

## Design Overview

- operator fusion algorithm from Relay to partition neural nets into subgraphs

**Program sampler** - two levels, sketch and annotate. High-level structure is sketched, low-level choices (tile size, unroll) are annotated. Randomly sample from the space.

**Performance tuner** - evolutionary search + cost model. Querying is much faster than evaluation.

**Task scheduler** - gradient-descent based scheduling algorithm to allocate resources to sub-graphs

### Program Sampler

Set of derivation rules to generate a sketch:
1. Skip
2. Always inline
3. Multi-level tiling - ⚠️ SSRSRS where "S" is one level of tile space and "R" is one level or reduction loops ⚠️
4. Tiling + fusion
5. Add cache stage
6. Reduction factorisation
7. User defined rules

Then we have a two step process: generate sketches by recursively applying sketch rules, and then annotate them.

Input is a partitioned subgraph:
- could be a naive loop nest
- could be a DAG

Generating for a DAG means topological order visit from output to input and iterative program construction.

Where there is data reuse, use tile and fusion. For element-wise ops like ReLU, we inline them. Can also add things like memory layout changes here.

Starting from `State(S,i)` of `S`= current program sketch and `i` current working node, work backwards through the graph and apply all of the derivation rules.

Since every state can have multiple successors, maintain a queue of possible intermediate states.

```
for i in range(I):
  c = c + a_i
```
dependence on `c`
  - reduction parallelism
  -

if you have a 6D loop with 3D tensor, you must have 3 reduction loops

# PR-HNSW: Reparación de Subgrafos Inducidos por Predicados para Búsqueda HNSW Filtrada

## 1. Resumen del proyecto

Este repositorio contiene el proyecto de tesis de maestría orientado al diseño, implementación y evaluación de **PR-HNSW**, una variante ligera y reproducible de HNSW para búsqueda vectorial filtrada en entornos con recursos limitados.

La idea central de la tesis es estudiar si la pérdida de `recall` en HNSW bajo filtros estrictos puede explicarse por la degradación topológica del subgrafo inducido por los predicados, y si una reparación selectiva bajo presupuesto puede mejorar la navegabilidad sin aumentar excesivamente memoria, latencia o complejidad de construcción.

Título tentativo:

> **Optimización de la Navegación en Grafos HNSW mediante Poda Dinámica y Reparación de Subgrafos Inducidos por Predicados para Consultas Híbridas en Entornos con Recursos Limitados**

---

## 2. Pregunta de investigación

¿Puede una estrategia ligera de reparación de subgrafos inducidos por predicados mejorar `recall@10` y latencia p95 en búsqueda HNSW filtrada bajo consultas híbridas con filtros estrictos, manteniendo un presupuesto acotado de memoria frente a post-filtrado, prefiltrado, reparación aleatoria y controles inspirados en ACORN?

---

## 3. Hipótesis principales

### H1 — Degradación del subgrafo inducido por predicados

Bajo filtros estrictos, HNSW pierde `recall` porque el subgrafo inducido por los nodos que cumplen el predicado se vuelve menos navegable: aumentan los componentes conectados, aparecen nodos aislados y disminuye el grado filtrado medio.

### H2 — Reparación selectiva

Una estrategia de reparación topológica mejora `recall@10` más que una reparación aleatoria bajo el mismo presupuesto de aristas o portales.

### H3 — Trade-off memoria-latencia

Una estrategia de reparación con presupuesto limitado puede recuperar `recall` con menor sobrecosto de memoria que estrategias densas o globales de expansión.

### H4 — La selectividad no es suficiente

La selectividad global del filtro no explica por sí sola la dificultad de la búsqueda filtrada. También deben medirse selectividad local, correlación GLS y conectividad del subgrafo inducido por predicados.

---

## 4. Enlaces importantes

### Documento de tesis en Overleaf

Visitar página:

```text
https://www.overleaf.com/project/6a2f0d202d5c85ff9553997a
```

### Capítulos de tesis dentro del repositorio

- [`tesis/capitulos/01_planteamiento_problema.tex`](tesis/capitulos/01_planteamiento_problema.tex)
- [`tesis/bibliografia/referencias.bib`](tesis/bibliografia/referencias.bib)

### Documentos metodológicos

- [`documentos/acta_investigacion.md`](documentos/acta_investigacion.md)
- [`documentos/metricas.md`](documentos/metricas.md)
- [`documentos/baselines.md`](documentos/baselines.md)
- [`documentos/reproducibilidad.md`](documentos/reproducibilidad.md)
- [`documentos/decisiones/`](documentos/decisiones/)

---

## 5. Corpus científico

El corpus se divide en tres niveles: corpus principal, corpus secundario y corpus de contexto. Esta división evita tratar todos los textos como si tuvieran el mismo peso dentro de la tesis.

### 5.1 Corpus principal

Estos textos sostienen directamente la pregunta de investigación, las hipótesis, los baselines y la contribución propuesta.

| Clave                          | Documento                                                                                                  | Función dentro de la tesis                                                               |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [`malkov2020hnsw`](https://ieeexplore.ieee.org/document/8594636)               | *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs* | Fundamento de HNSW                                                                       |
| [`patel2024acorn`](https://dl.acm.org/doi/10.1145/3654923)               | *ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data*               | Núcleo algorítmico de búsqueda híbrida y recorrido de subgrafos inducidos por predicados |
| [`amanbayev2026fanns`](https://arxiv.org/abs/2602.11443)           | *Filtered Approximate Nearest Neighbor Search in Vector Databases: System Design and Performance Analysis* | Taxonomía FANNS, sistemas vectoriales, GLS y benchmarking                                |
| [`gollapudi2023filtereddiskann`](https://arxiv.org/abs/2602.11443] | *Filtered-DiskANN: Graph Algorithms for Approximate Nearest Neighbor Search with Filters*                  | Baseline especializado de búsqueda filtrada                                              |
| [`diskann2019`](https://papers.nips.cc/paper_files/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html)                  | *DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node*                            | Referencia de escala, memoria, latencia y diseño ANN                                     |
| [`wang2021graphsurvey`](https://www.vldb.org/pvldb/vol14/p1964-wang.pdf)          | *A Comprehensive Survey and Experimental Comparison of Graph-Based Approximate Nearest Neighbor Search*    | Survey de graph-based ANNS, taxonomía y componentes                                      |


### 5.2 Corpus secundario

Estos documentos fortalecen el marco teórico, la discusión de baselines y la interpretación experimental.

| Tema                       | Ejemplos de textos                                                   |
| -------------------------- | -------------------------------------------------------------------- |
| Optimización de grafos ANN | Angular Distance-Guided Neighbor Selection, GraSP, FINGER, ParlayANN |
| Teoría de navegabilidad    | Navigable Graphs, graph-based NNS theory, query hardness             |
| Benchmarks FANNS           | Benchmarks de filtered vector search y evaluaciones multi-sistema    |
| Bases de datos vectoriales | Milvus, pgvector, Weaviate, Vespa, Qdrant, FAISS                     |
| Compresión y memoria       | PQ, SQ, IVF-PQ, quantization-aware ANN                               |


### 5.3 Corpus de contexto

Estos documentos ayudan en introducción, motivación o trabajo futuro, pero no deben dominar la contribución.

| Tema                   | Uso                                              |
| ---------------------- | ------------------------------------------------ |
| RAG                    | Motivación de recuperación semántica empresarial |
| Generative retrieval   | Contexto amplio de recuperación neuronal         |
| Cross-modal retrieval  | Contexto de embeddings multimodales              |
| Hardware especializado | Trabajo futuro, no núcleo del MVP científico     |
| Apple Silicon / UMA    | Discusión futura si la hipótesis se valida       |

---

## 6. Diccionario técnico del proyecto

### ANN / ANNS

**Approximate Nearest Neighbor Search**. Familia de métodos que buscan vecinos cercanos aproximados en lugar de calcular vecinos exactos mediante comparación exhaustiva.

Importancia: permite búsquedas eficientes en colecciones grandes de vectores.

### HNSW

**Hierarchical Navigable Small World**. Índice ANN basado en grafos jerárquicos navegables.

Importancia: es el punto de partida de la tesis y el índice que se modificará mediante diagnóstico y reparación topológica.

### FANNS

**Filtered Approximate Nearest Neighbor Search**. Búsqueda aproximada de vecinos más cercanos con restricciones adicionales sobre metadatos.

Importancia: representa el problema central de la tesis.

### Vector search

Búsqueda basada en similitud entre vectores. Normalmente usa distancia euclidiana, similitud coseno o producto interno.

Importancia: es la operación base de sistemas de búsqueda semántica, RAG y bases de datos vectoriales.

### Embedding

Representación vectorial densa de un objeto, como texto, imagen, audio o usuario.

Importancia: convierte datos no estructurados en objetos comparables geométricamente.

### Grafo

Estructura `G=(V,E)`, compuesta por vértices `V` y aristas `E`.

Importancia: HNSW y PR-HNSW se basan en grafos de proximidad.

### Subgrafo inducido por predicados

Subgrafo formado únicamente por los nodos que cumplen un predicado de filtrado.

Importancia: la hipótesis central afirma que su degradación topológica explica parte de la pérdida de `recall`.

### Predicado

Condición estructurada que define si un nodo es válido para una consulta.

Ejemplos: categoría, fecha, usuario, tenant, permiso, etiqueta.

### Selectividad

Proporción del dataset que cumple un predicado.

Importancia: filtros de baja selectividad suelen ser más difíciles para búsqueda filtrada.

### Selectividad local

Proporción de nodos válidos dentro del vecindario cercano de una consulta.

Importancia: puede explicar dificultad de búsqueda mejor que la selectividad global.

### GLS

**Global-Local Selectivity correlation**. Métrica que relaciona selectividad global y prevalencia local del filtro en vecindarios de consulta.

Importancia: ayuda a distinguir si la dificultad viene del sistema o de la distribución filtro-vector.

### Recall@k

Proporción de vecinos verdaderos recuperados entre los `k` resultados esperados.

Importancia: métrica principal de calidad de búsqueda.

### Latencia p95

Percentil 95 del tiempo de respuesta de consulta.

Importancia: representa comportamiento de cola y estabilidad del sistema.

### QPS

**Queries Per Second**. Número de consultas procesadas por segundo.

Importancia: métrica de throughput.

### Baseline

Método de referencia contra el cual se compara la propuesta.

Importancia: evita afirmar mejoras sin controles justos.

### Ground truth

Resultado exacto contra el cual se evalúa un método aproximado.

Importancia: permite calcular `recall@k`.

### Reparación topológica

Proceso de agregar o reorganizar conexiones del grafo para mejorar navegabilidad.

Importancia: es el mecanismo central propuesto por PR-HNSW.

### Portal

Nodo seleccionado como punto de entrada efectivo hacia un subgrafo filtrado.

Importancia: puede reducir fallos de entrada en filtros estrictos.

---

## 7. Fórmulas comunes del proyecto

### 7.1 Objetivo de búsqueda filtrada

Dado un conjunto de vectores:

```math
X = \{x_1, x_2, \ldots, x_n\}
```

y un predicado `p`, el subconjunto válido es:

```math
X_p = \{x_i \in X \mid p(x_i) = 1\}
```

La búsqueda filtrada busca los `k` vecinos más cercanos de una consulta `q` dentro de `X_p`, no dentro de todo `X`.

Importancia: define formalmente el problema central de la tesis.

### 7.2 Subgrafo inducido por predicados

Dado un grafo:

```math
G = (V,E)
```

y el conjunto de nodos válidos:

```math
V_p = \{v \in V \mid p(v)=1\}
```

el subgrafo inducido es:

```math
G_p = G[V_p]
```

Importancia: PR-HNSW estudia si `G_p` pierde navegabilidad bajo filtros estrictos.

### 7.3 Recall@k

Si `R_k(q)` es el conjunto exacto de vecinos filtrados verdaderos y `R_hat_k(q)` es el conjunto recuperado por el algoritmo:

```math
Recall@k(q) = \frac{|R_k(q) \cap \hat{R}_k(q)|}{k}
```

Importancia: mide la calidad de recuperación.

### 7.4 Selectividad global

```math
s_p = \frac{|V_p|}{|V|}
```

Importancia: mide qué fracción del dataset cumple un filtro.

### 7.5 Grado filtrado medio

```math
\bar{d}_p = \frac{1}{|V_p|}\sum_{v \in V_p} |\{u \in N(v) \mid u \in V_p\}|
```

Importancia: mide cuántas conexiones válidas conserva el subgrafo filtrado.

### 7.6 Razón de nodos aislados

```math
r_{iso} = \frac{|\{v \in V_p \mid d_p(v)=0\}|}{|V_p|}
```

Importancia: cuantifica nodos válidos que no tienen vecinos válidos dentro del subgrafo filtrado.

### 7.7 Razón del componente principal

```math
r_{main} = \frac{|C_{max}|}{|V_p|}
```

donde `C_max` es el componente conectado más grande de `G_p`.

Importancia: mide si el filtro conserva una región navegable dominante.

### 7.8 Latencia p95

```math
p95 = Percentil_{95}(\{t_1,t_2,\ldots,t_m\})
```

Importancia: mide estabilidad de tiempo de respuesta en la cola de la distribución.

### 7.9 Sobrecosto de memoria

```math
MemoryOverhead = \frac{Memory_{método} - Memory_{baseline}}{Memory_{baseline}}
```

Importancia: permite evaluar si una mejora de recall justifica el costo adicional de memoria.

---

## 8. Estructura del repositorio

```text
pr-hnsw/
├── README.md
├── pyproject.toml
├── Makefile
├── configuraciones/
├── documentos/
├── tesis/
├── src/
├── pruebas/
├── experimentos/
├── resultados/
└── scripts/
```

---

## 9. Reglas de reproducibilidad

Cada experimento debe registrar dataset, versión, semillas, configuración YAML, commit de Git, hardware, dependencias, salida cruda y comando exacto de ejecución.

---

## 10. Advertencia de integridad científica

Este proyecto no debe reportar mejoras no verificadas, referencias inventadas, baselines débiles, configuraciones ocultas ni resultados irreproducibles.

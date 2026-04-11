---
name: database-design
description: Expertise in designing efficient, scalable, and normalized relational or non-relational databases. Use when creating new schemas or optimizing existing database structures.
---

# Database Design

## Principles
- **Normalization**: Aim for 3NF (Third Normal Form) to reduce redundancy.
- **Indexing**: Carefully index columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses. Avoid over-indexing.
- **Data Integrity**: Use foreign keys, unique constraints, and check constraints to maintain data quality.
- **Scalability**: Consider partitioning, sharding, or read replicas for high-load systems.

## Workflow
1. **Requirements Analysis**: Identify the entities, attributes, and relationships.
2. **Conceptual Design**: Create an ER (Entity-Relationship) diagram.
3. **Logical Design**: Translate the ER diagram into tables, columns, and keys.
4. **Physical Design**: Choose data types, storage engines, and initial indexing strategy.
5. **Optimization**: Analyze query plans and adjust the schema/indexes as needed.

## Common Patterns
- **Soft Deletes**: Use a `deleted_at` column instead of hard deleting records.
- **Audit Logs**: Track changes to sensitive data with an audit table.
- **JSON Fields**: Use sparingly for semi-structured data in relational databases.

## Anti-Patterns
- **God Tables**: Tables with dozens or hundreds of columns.
- **EAV (Entity-Attribute-Value)**: Overly generic schemas that are hard to query and index.
- **Missing Foreign Keys**: Leads to orphaned records and data inconsistency.
- **Hard-coding Enums**: Prefer a reference table or a strict `CHECK` constraint.

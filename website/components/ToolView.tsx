import React from 'react';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { Tool } from '@/lib/yaml';
import { Star, ChevronLeft } from 'lucide-react';
import styles from '../app/tool/[slug]/page.module.css';

interface ToolViewProps {
  tool: Tool | undefined;
  locale?: string;
}

export default function ToolView({ tool, locale = 'zh' }: ToolViewProps) {
  if (!tool) {
    notFound();
  }

  const isEn = locale === 'en';
  const prefix = isEn ? '/en' : '';
  const desc = isEn ? (tool.description_en || tool.description) : tool.description;

  return (
    <div className={styles.container}>
      <Link href={`${prefix}/explore`} className={styles.backLink}>
        <ChevronLeft size={16} /> {isEn ? "Back to Explore" : "返回探索页"}
      </Link>

      <div className={styles.header}>
        <div className={styles.titleWrapper}>
          <h1 className={styles.title}>{tool.name}</h1>
          {tool.stars !== undefined && (
            <div className={styles.stars}>
              <Star size={18} fill="currentColor" />
              <span>{tool.stars.toLocaleString()}</span>
            </div>
          )}
        </div>
        
        {desc && (
          <p className={styles.description}>{desc}</p>
        )}
      </div>

      <div className={styles.metaGrid}>
        <div className={styles.metaItem}>
          <span className={styles.metaLabel}>{isEn ? "Category" : "分类"}</span>
          <span className={styles.metaValue}>{tool.category || (isEn ? 'Uncategorized' : '未分类')}</span>
        </div>
        
        {tool.language && (
          <div className={styles.metaItem}>
            <span className={styles.metaLabel}>{isEn ? "Language" : "语言"}</span>
            <span className={styles.metaValue}>{tool.language}</span>
          </div>
        )}
        
        {tool.license && (
          <div className={styles.metaItem}>
            <span className={styles.metaLabel}>{isEn ? "License" : "开源协议"}</span>
            <span className={styles.metaValue}>{tool.license}</span>
          </div>
        )}
        
        {tool.type && (
          <div className={styles.metaItem}>
            <span className={styles.metaLabel}>{isEn ? "Type" : "类型"}</span>
            <span className={styles.metaValue}>{tool.type === 'open' ? (isEn ? 'Open Source' : '开源') : (isEn ? 'Closed Source' : '闭源/商业')}</span>
          </div>
        )}
      </div>

      {tool.tags && tool.tags.length > 0 && (
        <div className={styles.section}>
          <h2>{isEn ? "Tags" : "标签"}</h2>
          <div>
            {tool.tags.map((tag) => (
              <span key={tag} className={styles.tag}>{tag}</span>
            ))}
          </div>
        </div>
      )}

      {tool.highlights && tool.highlights.length > 0 && (
        <div className={styles.section}>
          <h2>{isEn ? "Highlights" : "核心亮点"}</h2>
          <ul className={styles.highlightsList}>
            {tool.highlights.map((highlight, index) => (
              <li key={index}>{highlight}</li>
            ))}
          </ul>
        </div>
      )}

      <div className={styles.actions}>
        {tool.url && (
          <a href={tool.url} target="_blank" rel="noreferrer" className={`${styles.btn} ${styles.primaryBtn}`}>
            {isEn ? "Visit Website" : "访问官网"}
          </a>
        )}
        {tool.repo && (
          <a href={tool.repo} target="_blank" rel="noreferrer" className={`${styles.btn} ${styles.secondaryBtn}`}>
            {isEn ? "View GitHub Repo" : "查看 GitHub 仓库"}
          </a>
        )}
      </div>
    </div>
  );
}

import React from 'react';
import Link from 'next/link';
import { Star, Globe } from 'lucide-react';
import styles from './ToolCard.module.css';
import { Tool } from '../lib/yaml';

interface ToolCardProps {
  tool: Tool;
  locale?: string;
}

function formatStars(stars: number | undefined) {
  if (!stars) return '0';
  if (stars >= 1000) {
    return (stars / 1000).toFixed(1) + 'k';
  }
  return stars.toString();
}

export default function ToolCard({ tool, locale = 'zh' }: ToolCardProps) {
  const isEn = locale === 'en';
  const prefix = isEn ? '/en' : '';
  const desc = isEn ? (tool.description_en || tool.description) : tool.description;

  return (
    <div className={styles.card}>
      <div className={styles.header}>
        <Link href={`${prefix}/tool/${tool.slug}`} className={styles.title}>
          {tool.name}
        </Link>
        {tool.stars !== undefined && (
          <div className={styles.stars}>
            <Star size={14} fill="currentColor" />
            <span>{formatStars(tool.stars)}</span>
          </div>
        )}
      </div>
      
      <p className={styles.description}>
        {desc || (isEn ? 'No description available' : '暂无描述信息')}
      </p>
      
      <div className={styles.footer}>
        <div className={styles.tags}>
          {tool.tags?.slice(0, 3).map(tag => (
            <span key={tag} className={styles.tag}>{tag}</span>
          ))}
        </div>
        
        <div className={styles.links}>
          {tool.repo && (
            <a href={tool.repo} target="_blank" rel="noreferrer" className={styles.link} title="GitHub Repo">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
              </svg>
            </a>
          )}
          {tool.url && (
            <a href={tool.url} target="_blank" rel="noreferrer" className={styles.link} title="Website">
              <Globe size={18} />
            </a>
          )}
        </div>
      </div>
    </div>
  );
}
